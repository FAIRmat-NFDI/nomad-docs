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
                currentGroup = {
                    mainRow: row,
                    detailRow: null,
                    types: [],
                    ownerNormalized: "",
                    ownerDisplay: "",
                    pluginName: "",
                    stars: 0
                };
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

        function extractOwnerInfo(mainRow, detailRow) {
            if (mainRow.dataset.owner) {
                const owner = (mainRow.dataset.owner || "").trim();
                return { normalized: normalize(owner), display: owner };
            }

            if (!detailRow) {
                return { normalized: "", display: "" };
            }

            const ownerLabel = Array.from(detailRow.querySelectorAll("strong")).find((node) =>
                normalize(node.textContent).startsWith("owner:")
            );
            if (!ownerLabel) {
                return { normalized: "", display: "" };
            }

            let textNode = ownerLabel.nextSibling;
            while (textNode && !(textNode.textContent || "").trim()) {
                textNode = textNode.nextSibling;
            }
            const owner = ((textNode && textNode.textContent) || "").trim();
            return { normalized: normalize(owner), display: owner };
        }

        function extractPluginName(mainRow) {
            if (mainRow.dataset.pluginName) {
                return (mainRow.dataset.pluginName || "").trim();
            }
            const strong = mainRow.querySelector("td strong");
            if (!strong) {
                return "";
            }
            return (strong.textContent || "").trim();
        }

        function extractStars(mainRow) {
            if (mainRow.dataset.stars) {
                const parsed = Number.parseInt(mainRow.dataset.stars, 10);
                return Number.isFinite(parsed) ? parsed : 0;
            }
            const firstCell = mainRow.querySelector("td");
            const text = (firstCell?.textContent || "");
            const match = text.match(/⭐\s*(\d+)/);
            if (!match) {
                return 0;
            }
            const parsed = Number.parseInt(match[1], 10);
            return Number.isFinite(parsed) ? parsed : 0;
        }

        function isFairmatOwner(ownerNormalized) {
            return ["fairmat-nfdi", "nomad-coe", "nomadcoe"].includes(ownerNormalized);
        }

        groupedRows.forEach((group) => {
            group.types = extractTypes(group.mainRow);
            const ownerInfo = extractOwnerInfo(group.mainRow, group.detailRow);
            group.ownerNormalized = ownerInfo.normalized;
            group.ownerDisplay = ownerInfo.display;
            group.pluginName = extractPluginName(group.mainRow);
            group.stars = extractStars(group.mainRow);
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
                .map((word) => {
                    const normalizedWord = normalize(word);
                    if (normalizedWord === "api") {
                        return "API";
                    }
                    return word ? word.charAt(0).toUpperCase() + word.slice(1) : "";
                })
                .join(" ");
        }

        function formatLegendLabel(label) {
            if (normalize(label) === "fairmat") {
                return "FAIRmat";
            }
            if (normalize(label) === "unknown") {
                return "Unknown";
            }
            return titleCase(label);
        }

        function findPreviousSiblingWithAttr(startNode, attrName) {
            let node = startNode.previousElementSibling;
            while (node && !node.hasAttribute(attrName)) {
                node = node.previousElementSibling;
            }
            return node;
        }

        function enableClickToggleMultiSelect(selectNode) {
            if (!selectNode || !selectNode.multiple || selectNode.dataset.clickToggleInit === "true") {
                return;
            }
            selectNode.dataset.clickToggleInit = "true";
            selectNode.addEventListener("mousedown", (event) => {
                const option = event.target.closest("option");
                if (!option) {
                    return;
                }
                event.preventDefault();
                option.selected = !option.selected;
                selectNode.dispatchEvent(new Event("change", { bubbles: true }));
            });
        }

        let filterRoot = findPreviousSiblingWithAttr(table, "data-plugin-registry-filter");
        if (!filterRoot) {
            filterRoot = document.createElement("div");
            filterRoot.className = "plugin-registry-filter";
            filterRoot.setAttribute("data-plugin-registry-filter", "true");
            table.parentNode.insertBefore(filterRoot, table);
        }

        let filterLabel = filterRoot.querySelector(".plugin-registry-filter__label--type");
        if (!filterLabel) {
            filterLabel = document.createElement("label");
            filterLabel.className = "plugin-registry-filter__label plugin-registry-filter__label--type";
            filterLabel.textContent = "Containing";
            filterRoot.appendChild(filterLabel);
        }

        let filterSelect = filterRoot.querySelector(".plugin-registry-filter__type");
        if (!filterSelect) {
            filterSelect = document.createElement("select");
            filterSelect.className = "plugin-registry-filter__select plugin-registry-filter__type";
            filterRoot.appendChild(filterSelect);
        }
        filterSelect.multiple = true;
        if (!filterSelect.hasAttribute("size")) {
            filterSelect.size = 4;
        }

        let ownerLabel = filterRoot.querySelector(".plugin-registry-filter__label--owner");
        if (!ownerLabel) {
            ownerLabel = document.createElement("label");
            ownerLabel.className = "plugin-registry-filter__label plugin-registry-filter__label--owner";
            ownerLabel.textContent = "Owner";
            filterRoot.appendChild(ownerLabel);
        }

        let ownerSelect = filterRoot.querySelector(".plugin-registry-filter__owner");
        if (!ownerSelect) {
            ownerSelect = document.createElement("select");
            ownerSelect.className = "plugin-registry-filter__select plugin-registry-filter__owner";
            filterRoot.appendChild(ownerSelect);
        }
        ownerSelect.multiple = true;
        if (!ownerSelect.hasAttribute("size")) {
            ownerSelect.size = 4;
        }

        let sortLabel = filterRoot.querySelector(".plugin-registry-filter__label--sort");
        if (!sortLabel) {
            sortLabel = document.createElement("label");
            sortLabel.className = "plugin-registry-filter__label plugin-registry-filter__label--sort";
            sortLabel.textContent = "Sort";
            filterRoot.appendChild(sortLabel);
        }

        let sortSelect = filterRoot.querySelector(".plugin-registry-filter__sort");
        if (!sortSelect) {
            sortSelect = document.createElement("select");
            sortSelect.className = "plugin-registry-filter__select plugin-registry-filter__sort";
            filterRoot.appendChild(sortSelect);
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
        if (countNode.parentElement === filterRoot) {
            filterRoot.appendChild(countNode);
        }

        if (!filterSelect.id) {
            filterSelect.id = `plugin-registry-type-filter-${tableIndex}`;
        }
        filterLabel.setAttribute("for", filterSelect.id);
        if (!ownerSelect.id) {
            ownerSelect.id = `plugin-registry-owner-filter-${tableIndex}`;
        }
        ownerLabel.setAttribute("for", ownerSelect.id);
        if (!sortSelect.id) {
            sortSelect.id = `plugin-registry-sort-${tableIndex}`;
        }
        sortLabel.setAttribute("for", sortSelect.id);
        enableClickToggleMultiSelect(filterSelect);
        enableClickToggleMultiSelect(ownerSelect);

        let noticeNode = findPreviousSiblingWithAttr(table, "data-plugin-registry-notice");
        if (!noticeNode) {
            noticeNode = document.createElement("div");
            noticeNode.className = "plugin-registry-notice";
            noticeNode.setAttribute("data-plugin-registry-notice", "true");
            noticeNode.setAttribute("aria-live", "polite");
            table.parentNode.insertBefore(noticeNode, table);
        }

        let chartRoot = findPreviousSiblingWithAttr(table, "data-plugin-registry-chart");
        if (!chartRoot) {
            chartRoot = document.createElement("div");
            chartRoot.className = "plugin-registry-chart";
            chartRoot.setAttribute("data-plugin-registry-chart", "true");
            table.parentNode.insertBefore(chartRoot, table);
        }

        const chartPanelsMarkup = `
            <p class="plugin-registry-chart__title"><strong>Filtered Distributions</strong></p>
            <div class="plugin-registry-chart__panels">
                <section class="plugin-registry-chart__panel" data-chart-kind="type">
                    <p class="plugin-registry-chart__panel-title"><strong>Entry Point Type</strong></p>
                    <div class="plugin-registry-chart__panel-content">
                        <div class="plugin-registry-chart__pie-wrap">
                            <div class="plugin-registry-chart__pie" role="img" aria-label="Plugin type distribution pie chart">
                                <span class="plugin-registry-chart__pie-total">0</span>
                            </div>
                        </div>
                        <div class="plugin-registry-chart__legend"></div>
                    </div>
                </section>
                <section class="plugin-registry-chart__panel" data-chart-kind="owner">
                    <p class="plugin-registry-chart__panel-title"><strong>Owner</strong></p>
                    <div class="plugin-registry-chart__panel-content">
                        <div class="plugin-registry-chart__pie-wrap">
                            <div class="plugin-registry-chart__pie" role="img" aria-label="Plugin owner distribution pie chart">
                                <span class="plugin-registry-chart__pie-total">0</span>
                            </div>
                        </div>
                        <div class="plugin-registry-chart__legend"></div>
                    </div>
                </section>
            </div>`;

        const hasTypePanel = !!chartRoot.querySelector('[data-chart-kind="type"]');
        const hasOwnerPanel = !!chartRoot.querySelector('[data-chart-kind="owner"]');
        if (!hasTypePanel || !hasOwnerPanel) {
            chartRoot.innerHTML = chartPanelsMarkup;
        }

        if (filterRoot.nextElementSibling !== chartRoot) {
            filterRoot.insertAdjacentElement("afterend", chartRoot);
        }
        if (filterRoot.nextElementSibling !== noticeNode) {
            filterRoot.insertAdjacentElement("afterend", noticeNode);
        }
        if (noticeNode.nextElementSibling !== chartRoot) {
            noticeNode.insertAdjacentElement("afterend", chartRoot);
        }

        const typePanel = chartRoot.querySelector('[data-chart-kind="type"]');
        const ownerPanel = chartRoot.querySelector('[data-chart-kind="owner"]');
        const typePieNode = typePanel?.querySelector(".plugin-registry-chart__pie");
        const typePieTotalNode = typePanel?.querySelector(".plugin-registry-chart__pie-total");
        const typePieLegendNode = typePanel?.querySelector(".plugin-registry-chart__legend");
        const ownerPieNode = ownerPanel?.querySelector(".plugin-registry-chart__pie");
        const ownerPieTotalNode = ownerPanel?.querySelector(".plugin-registry-chart__pie-total");
        const ownerPieLegendNode = ownerPanel?.querySelector(".plugin-registry-chart__legend");

        function renderPieChart(pieNode, pieTotalNode, pieLegendNode, countsMap, totalValue, labelBase) {
            if (!pieNode || !pieTotalNode || !pieLegendNode) {
                return;
            }

            const sortedCounts = Array.from(countsMap.entries()).sort((a, b) => b[1] - a[1]);
            const totalSlices = sortedCounts.reduce((sum, [, count]) => sum + count, 0);

            if (!sortedCounts.length || totalSlices <= 0) {
                pieNode.style.background = "var(--plugin-registry-pie-empty-bg)";
                pieLegendNode.innerHTML = '<p class="plugin-registry-chart__empty">No visible items.</p>';
                pieTotalNode.textContent = "0";
                pieNode.setAttribute("aria-label", `${labelBase} pie chart: no visible items`);
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
            pieTotalNode.textContent = `${totalValue}`;
            pieNode.setAttribute(
                "aria-label",
                `${labelBase} pie chart for ${totalValue} visible plugins`
            );

            pieLegendNode.innerHTML = sortedCounts
                .map(([label, count], index) => {
                    const color = chartColors[index % chartColors.length];
                    return `<div class="plugin-registry-chart__legend-item">
                        <span class="plugin-registry-chart__legend-swatch" style="background:${color}"></span>
                        <span class="plugin-registry-chart__legend-label">${formatLegendLabel(label)}</span>
                        <span class="plugin-registry-chart__legend-value">${count}</span>
                    </div>`;
                })
                .join("");
        }

        filterSelect.innerHTML = "";
        for (const type of availableTypes) {
            const option = document.createElement("option");
            option.value = type;
            option.textContent = titleCase(type);
            filterSelect.appendChild(option);
        }
        filterSelect.selectedIndex = -1;

        const OWNER_FILTER_MIN_COUNT = 5;
        const majorOwnerDisplayByNormalized = new Map();
        const ownerCountsByNormalized = new Map();
        let hasFairmatOwners = false;
        let hasNonFairmatOwners = false;
        groupedRows.forEach((group) => {
            if (!group.ownerNormalized) {
                return;
            }
            ownerCountsByNormalized.set(
                group.ownerNormalized,
                (ownerCountsByNormalized.get(group.ownerNormalized) || 0) + 1
            );
            if (isFairmatOwner(group.ownerNormalized)) {
                hasFairmatOwners = true;
            } else {
                hasNonFairmatOwners = true;
            }
        });

        groupedRows.forEach((group) => {
            if (!group.ownerNormalized || isFairmatOwner(group.ownerNormalized)) {
                return;
            }
            if ((ownerCountsByNormalized.get(group.ownerNormalized) || 0) < OWNER_FILTER_MIN_COUNT) {
                return;
            }
            if (!majorOwnerDisplayByNormalized.has(group.ownerNormalized)) {
                majorOwnerDisplayByNormalized.set(group.ownerNormalized, group.ownerDisplay);
            }
        });
        const sortedOtherOwners = Array.from(majorOwnerDisplayByNormalized.entries())
            .sort((a, b) => a[1].localeCompare(b[1]));

        ownerSelect.innerHTML = "";
        if (hasFairmatOwners) {
            const fairmatOption = document.createElement("option");
            fairmatOption.value = "__fairmat__";
            fairmatOption.textContent = "FAIRmat";
            ownerSelect.appendChild(fairmatOption);
        }
        if (hasNonFairmatOwners) {
            const nonFairmatOption = document.createElement("option");
            nonFairmatOption.value = "__non_fairmat__";
            nonFairmatOption.textContent = "Non-FAIRmat";
            ownerSelect.appendChild(nonFairmatOption);
        }
        sortedOtherOwners.forEach(([normalizedOwner, ownerDisplay]) => {
            const option = document.createElement("option");
            option.value = normalizedOwner;
            option.textContent = ownerDisplay;
            ownerSelect.appendChild(option);
        });
        ownerSelect.selectedIndex = -1;

        sortSelect.innerHTML = "";
        [
            { value: "name_asc", label: "Name (A→Z)" },
            { value: "name_desc", label: "Name (Z→A)" },
            { value: "stars_desc", label: "Stars (high→low)" }
        ].forEach((entry) => {
            const option = document.createElement("option");
            option.value = entry.value;
            option.textContent = entry.label;
            sortSelect.appendChild(option);
        });
        sortSelect.value = "name_asc";

        function getSelectedValues(selectNode) {
            return new Set(
                Array.from(selectNode.selectedOptions || [])
                    .map((option) => normalize(option.value))
                    .filter(Boolean)
            );
        }

        function applyFilter() {
            const selectedTypes = getSelectedValues(filterSelect);
            const selectedOwners = getSelectedValues(ownerSelect);
            const selectedSort = normalize(sortSelect.value || "name_asc");
            const sortedGroups = [...groupedRows].sort((a, b) => {
                if (selectedSort === "name_desc") {
                    return b.pluginName.localeCompare(a.pluginName, undefined, { sensitivity: "base" });
                }
                if (selectedSort === "stars_desc") {
                    if (b.stars !== a.stars) {
                        return b.stars - a.stars;
                    }
                    return a.pluginName.localeCompare(b.pluginName, undefined, { sensitivity: "base" });
                }
                return a.pluginName.localeCompare(b.pluginName, undefined, { sensitivity: "base" });
            });
            let shownCount = 0;
            const totalCount = groupedRows.length;
            const visibleTypeCounts = new Map();
            const visibleOwnerCounts = new Map();
            let shownFairmatCount = 0;
            let shownNonFairmatCount = 0;

            sortedGroups.forEach((group) => {
                const matchesType =
                    selectedTypes.size === 0
                    || group.types.some((type) => selectedTypes.has(type));
                const matchesOwner =
                    selectedOwners.size === 0
                    || (
                        selectedOwners.has("__fairmat__")
                        && isFairmatOwner(group.ownerNormalized)
                    )
                    || (
                        selectedOwners.has("__non_fairmat__")
                        && !isFairmatOwner(group.ownerNormalized)
                    )
                    || selectedOwners.has(group.ownerNormalized);
                const matches = matchesType && matchesOwner;

                tbody.appendChild(group.mainRow);
                if (group.detailRow) {
                    tbody.appendChild(group.detailRow);
                }
                group.mainRow.style.display = matches ? "" : "none";
                if (group.detailRow) {
                    group.detailRow.style.display = matches ? "" : "none";
                }
                if (matches) {
                    shownCount += 1;
                    group.types.forEach((type) => {
                        visibleTypeCounts.set(type, (visibleTypeCounts.get(type) || 0) + 1);
                    });
                    let ownerBucket = "other";
                    if (isFairmatOwner(group.ownerNormalized)) {
                        shownFairmatCount += 1;
                        ownerBucket = "fairmat";
                    } else if (majorOwnerDisplayByNormalized.has(group.ownerNormalized)) {
                        shownNonFairmatCount += 1;
                        ownerBucket = majorOwnerDisplayByNormalized.get(group.ownerNormalized);
                    } else {
                        shownNonFairmatCount += 1;
                    }
                    visibleOwnerCounts.set(
                        ownerBucket,
                        (visibleOwnerCounts.get(ownerBucket) || 0) + 1
                    );
                }
            });

            noticeNode.classList.remove(
                "plugin-registry-notice--warning",
                "plugin-registry-notice--success"
            );
            if (shownCount === 0) {
                noticeNode.style.display = "none";
                noticeNode.textContent = "";
            } else if (shownNonFairmatCount > 0) {
                noticeNode.style.display = "";
                noticeNode.classList.add("plugin-registry-notice--warning");
                noticeNode.textContent =
                    "Warning: This selection includes non-FAIRmat plugins. FAIRmat has not checked these plugins for validity or compatibility with the latest NOMAD version.";
            } else if (shownFairmatCount > 0) {
                noticeNode.style.display = "";
                noticeNode.classList.add("plugin-registry-notice--success");
                noticeNode.textContent =
                    "All currently shown plugins are developed and maintained by FAIRmat.";
            }

            countNode.textContent = `${shownCount}/${totalCount} plugins shown`;
            renderPieChart(
                typePieNode,
                typePieTotalNode,
                typePieLegendNode,
                visibleTypeCounts,
                shownCount,
                "Plugin type distribution"
            );
            renderPieChart(
                ownerPieNode,
                ownerPieTotalNode,
                ownerPieLegendNode,
                visibleOwnerCounts,
                shownCount,
                "Plugin owner distribution"
            );
        }

        filterSelect.addEventListener("change", applyFilter);
        ownerSelect.addEventListener("change", applyFilter);
        sortSelect.addEventListener("change", applyFilter);
        clearButton.addEventListener("click", () => {
            Array.from(filterSelect.options).forEach((option) => {
                option.selected = false;
            });
            Array.from(ownerSelect.options).forEach((option) => {
                option.selected = false;
            });
            sortSelect.value = "name_asc";
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
