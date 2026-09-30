function initializeDiagramZoom() {
    const diagrams = document.querySelectorAll("[data-diagram-zoom]");

    diagrams.forEach((diagram) => {
        if (diagram.dataset.diagramZoomInitialized === "true") return;

        diagram.dataset.diagramZoomInitialized = "true";
        diagram.tabIndex = 0;
        diagram.setAttribute("role", "button");
        diagram.setAttribute("aria-expanded", "false");

        const setZoomed = (zoomed) => {
            diagram.classList.toggle("is-zoomed", zoomed);
            diagram.setAttribute("aria-expanded", String(zoomed));
        };

        diagram.addEventListener("click", () => {
            setZoomed(!diagram.classList.contains("is-zoomed"));
        });

        diagram.addEventListener("keydown", (event) => {
            if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                setZoomed(!diagram.classList.contains("is-zoomed"));
            } else if (event.key === "Escape") {
                setZoomed(false);
            }
        });
    });
}

document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;

    document.querySelectorAll("[data-diagram-zoom].is-zoomed").forEach((diagram) => {
        diagram.classList.remove("is-zoomed");
        diagram.setAttribute("aria-expanded", "false");
    });
});

if (typeof document$ !== "undefined") {
    document$.subscribe(initializeDiagramZoom);
} else {
    document.addEventListener("DOMContentLoaded", initializeDiagramZoom);
}
