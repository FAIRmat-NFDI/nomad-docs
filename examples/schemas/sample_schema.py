from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.datamodel.metainfo.annotations import ELNAnnotation
from nomad.metainfo import Datetime, MEnum, Quantity, SchemaPackage, SubSection

m_package = SchemaPackage()


class Instrument(EntryData):
    """A piece of equipment used to carry out a process."""

    name = Quantity(
        type=str,
        description='The name this instrument is known by in the lab.',
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )


class Process(ArchiveSection):
    """A single step carried out on a sample."""

    start_time = Quantity(
        type=Datetime,
        description='When the process was started.',
        a_eln=ELNAnnotation(component='DateTimeEditQuantity'),
    )
    instrument = Quantity(
        type=Instrument,
        description='The instrument used for this process.',
        a_eln=ELNAnnotation(component='ReferenceEditQuantity'),
    )


class Evaporation(Process):
    """Depositing a material onto the sample from the vapour phase."""

    chamber_pressure = Quantity(
        type=float,
        unit='pascal',
        description='The pressure in the chamber during evaporation.',
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )


class Annealing(Process):
    """Heating the sample to change its structure."""

    temperature = Quantity(
        type=float,
        unit='kelvin',
        description='The temperature the sample was held at.',
        a_eln=ELNAnnotation(component='NumberEditQuantity'),
    )


class Sample(EntryData):
    """A specimen that a sequence of processes is carried out on."""

    name = Quantity(
        type=str,
        description='A short name for this sample.',
        a_eln=ELNAnnotation(component='StringEditQuantity'),
    )
    substrate_type = Quantity(
        type=MEnum('silicon', 'glass', 'sapphire'),
        description='The material the sample was grown on.',
        a_eln=ELNAnnotation(component='EnumEditQuantity'),
    )
    tags = Quantity(
        type=str,
        shape=['*'],
        description='Free-form labels used to group samples.',
    )
    sample_id = Quantity(
        type=str,
        description='An identifier derived from the name and the first process.',
    )

    processes = SubSection(section=Process, repeats=True)

    def normalize(self, archive, logger):
        super().normalize(archive, logger)

        if self.sample_id is None and self.name is not None:
            self.sample_id = f'{self.name}--{len(self.processes)}'


m_package.__init_metainfo__()
