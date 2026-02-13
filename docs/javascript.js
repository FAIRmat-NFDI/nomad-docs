function setHeaderButtonTitle() {
    const headerButton = document.getElementsByClassName("md-header__button")[0];
    if (headerButton) {
        headerButton.title = "NOMAD";
    }
}

function initImageSliders() {
    const sliders = document.querySelectorAll(".image-slider");

    sliders.forEach((slider) => {
        if (slider.dataset.sliderInit === "true") {
            return;
        }
        slider.dataset.sliderInit = "true";

        const images = slider.querySelectorAll("img");
        const prevButton = slider.querySelector(".nav-arrow.left");
        const nextButton = slider.querySelector(".nav-arrow.right");
        let currentImageIndex = 0;

        if (!images.length || !prevButton || !nextButton) {
            return;
        }

        images[currentImageIndex].classList.add("active");

        nextButton.addEventListener("click", () => {
            images[currentImageIndex].classList.remove("active");
            currentImageIndex = (currentImageIndex + 1) % images.length;
            images[currentImageIndex].classList.add("active");
        });

        prevButton.addEventListener("click", () => {
            images[currentImageIndex].classList.remove("active");
            currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
            images[currentImageIndex].classList.add("active");
        });
    });
}

function initPluginRegistryFilters() {
    const tables = Array.from(
        document.querySelectorAll('table[data-plugin-registry="true"], table.plugin-registry-table')
    );

    tables.forEach((table, tableIndex) => {
        if (table.dataset.pluginRegistryInit === "true") {
            return;
        }
        table.dataset.pluginRegistryInit = "true";

        const tbody = table.querySelector("tbody");
        if (!tbody) {
            return;
        }

        const groupedRows = [];
        let currentGroup = null;
        const bodyRows = Array.from(tbody.querySelectorAll("tr"));

        for (const row of bodyRows) {
            const isDetailsRow =
                row.classList.contains("plugin-registry-row--details") ||
                row.querySelector("details");

            if (!isDetailsRow) {
                currentGroup = { mainRow: row, detailRow: null, types: [] };
                groupedRows.push(currentGroup);
            } else if (currentGroup && !currentGroup.detailRow) {
                currentGroup.detailRow = row;
            }
        }

        function normalize(value) {
            return (value || "").toString().trim().toLowerCase();
        }

        function extractTypes(mainRow) {
            if (mainRow.dataset.entryPointTypes) {
                return mainRow.dataset.entryPointTypes
                    .split("|")
                    .map((item) => normalize(item))
                    .filter(Boolean);
            }

            const typeNode = mainRow.querySelector("td small");
            if (!typeNode) {
                return [];
            }

            return typeNode.textContent
                .split(",")
                .map((item) => normalize(item))
                .filter((item) => item && item !== "—");
        }

        groupedRows.forEach((group) => {
            group.types = extractTypes(group.mainRow);
        });

        const availableTypes = Array.from(
            new Set(groupedRows.flatMap((group) => group.types))
        ).sort((a, b) => a.localeCompare(b));
        const chartColors = [
            "#2A4CDF",
            "#008A67",
            "#FF6B6B",
            "#4ECDC4",
            "#F4A261",
            "#E9C46A",
            "#A855F7",
            "#60A5FA",
            "#22C55E",
            "#FB7185"
        ];

        function titleCase(value) {
            return (value || "")
                .split(" ")
                .map((word) => word ? word.charAt(0).toUpperCase() + word.slice(1) : "")
                .join(" ");
        }

        function findPreviousSiblingWithAttr(startNode, attrName) {
            let node = startNode.previousElementSibling;
            while (node && !node.hasAttribute(attrName)) {
                node = node.previousElementSibling;
            }
            return node;
        }

        let filterRoot = findPreviousSiblingWithAttr(table, "data-plugin-registry-filter");
        if (!filterRoot) {
            filterRoot = document.createElement("div");
            filterRoot.className = "plugin-registry-filter";
            filterRoot.setAttribute("data-plugin-registry-filter", "true");
            table.parentNode.insertBefore(filterRoot, table);
        }

        let filterLabel = filterRoot.querySelector(".plugin-registry-filter__label");
        if (!filterLabel) {
            filterLabel = document.createElement("label");
            filterLabel.className = "plugin-registry-filter__label";
            filterLabel.textContent = "Containing";
            filterRoot.appendChild(filterLabel);
        }

        let filterSelect = filterRoot.querySelector(".plugin-registry-filter__select");
        if (!filterSelect) {
            filterSelect = document.createElement("select");
            filterSelect.className = "plugin-registry-filter__select";
            filterRoot.appendChild(filterSelect);
        }

        let clearButton = filterRoot.querySelector(".plugin-registry-filter__clear");
        if (!clearButton) {
            clearButton = document.createElement("button");
            clearButton.className = "plugin-registry-filter__clear";
            clearButton.type = "button";
            clearButton.textContent = "Clear";
            filterRoot.appendChild(clearButton);
        }

        let countNode = filterRoot.querySelector(".plugin-registry-filter__count");
        if (!countNode) {
            countNode = document.createElement("span");
            countNode.className = "plugin-registry-filter__count";
            countNode.setAttribute("aria-live", "polite");
            filterRoot.appendChild(countNode);
        }

        if (!filterSelect.id) {
            filterSelect.id = `plugin-registry-type-filter-${tableIndex}`;
        }
        filterLabel.setAttribute("for", filterSelect.id);

        let chartRoot = findPreviousSiblingWithAttr(table, "data-plugin-registry-chart");
        if (!chartRoot) {
            chartRoot = document.createElement("div");
            chartRoot.className = "plugin-registry-chart";
            chartRoot.setAttribute("data-plugin-registry-chart", "true");
            chartRoot.innerHTML = `
                <p class="plugin-registry-chart__title"><strong>Plugin Type Distribution (Filtered)</strong></p>
                <div class="plugin-registry-chart__content">
                    <div class="plugin-registry-chart__pie-wrap">
                        <div class="plugin-registry-chart__pie" role="img" aria-label="Plugin type distribution pie chart">
                            <span class="plugin-registry-chart__pie-total">0</span>
                        </div>
                    </div>
                    <div class="plugin-registry-chart__legend"></div>
                </div>`;
            table.parentNode.insertBefore(chartRoot, table);
        }

        if (filterRoot.nextElementSibling !== chartRoot) {
            filterRoot.insertAdjacentElement("afterend", chartRoot);
        }

        const pieNode = chartRoot.querySelector(".plugin-registry-chart__pie");
        const pieTotalNode = chartRoot.querySelector(".plugin-registry-chart__pie-total");
        const pieLegendNode = chartRoot.querySelector(".plugin-registry-chart__legend");

        const optionValues = new Set(
            Array.from(filterSelect.options).map((option) => normalize(option.value))
        );
        if (!optionValues.has("")) {
            const allOption = document.createElement("option");
            allOption.value = "";
            allOption.textContent = "All entry point types";
            filterSelect.appendChild(allOption);
        }
        for (const type of availableTypes) {
            if (!optionValues.has(type)) {
                const option = document.createElement("option");
                option.value = type;
                option.textContent = type
                    .split(" ")
                    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
                    .join(" ");
                filterSelect.appendChild(option);
            }
        }

        function applyFilter() {
            const selectedType = normalize(filterSelect.value);
            let shownCount = 0;
            const totalCount = groupedRows.length;
            const visibleTypeCounts = new Map();

            groupedRows.forEach((group) => {
                const matches =
                    !selectedType || group.types.some((type) => type === selectedType);

                group.mainRow.style.display = matches ? "" : "none";
                if (group.detailRow) {
                    group.detailRow.style.display = matches ? "" : "none";
                }
                if (matches) {
                    shownCount += 1;
                    group.types.forEach((type) => {
                        visibleTypeCounts.set(type, (visibleTypeCounts.get(type) || 0) + 1);
                    });
                }
            });

            countNode.textContent = `${shownCount} of ${totalCount} plugins shown`;

            const sortedCounts = Array.from(visibleTypeCounts.entries()).sort((a, b) => b[1] - a[1]);
            const totalSlices = sortedCounts.reduce((sum, [, count]) => sum + count, 0);

            if (pieNode && pieLegendNode && pieTotalNode) {
                if (!sortedCounts.length || totalSlices <= 0) {
                    pieNode.style.background = "#e5e7eb";
                    pieLegendNode.innerHTML = '<p class="plugin-registry-chart__empty">No visible plugin types.</p>';
                    pieTotalNode.textContent = "0";
                    return;
                }

                let running = 0;
                const segments = sortedCounts.map(([, count], index) => {
                    const start = (running / totalSlices) * 100;
                    running += count;
                    const end = (running / totalSlices) * 100;
                    const color = chartColors[index % chartColors.length];
                    return `${color} ${start}% ${end}%`;
                });
                pieNode.style.background = `conic-gradient(${segments.join(", ")})`;
                pieTotalNode.textContent = `${shownCount}`;
                pieNode.setAttribute(
                    "aria-label",
                    `Plugin type distribution pie chart for ${shownCount} visible plugins`
                );

                pieLegendNode.innerHTML = sortedCounts
                    .map(([type, count], index) => {
                        const color = chartColors[index % chartColors.length];
                        return `<div class="plugin-registry-chart__legend-item">
                            <span class="plugin-registry-chart__legend-swatch" style="background:${color}"></span>
                            <span class="plugin-registry-chart__legend-label">${titleCase(type)}</span>
                            <span class="plugin-registry-chart__legend-value">${count}</span>
                        </div>`;
                    })
                    .join("");
            }
        }

        filterSelect.addEventListener("change", applyFilter);
        clearButton.addEventListener("click", () => {
            filterSelect.value = "";
            applyFilter();
        });

        applyFilter();
    });
}

function initDocsEnhancements() {
    setHeaderButtonTitle();
    initImageSliders();
    initPluginRegistryFilters();
}

if (typeof window.document$ !== "undefined" && window.document$?.subscribe) {
    window.document$.subscribe(() => {
        initDocsEnhancements();
    });
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initDocsEnhancements);
} else {
    initDocsEnhancements();
}
