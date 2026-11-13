
document.addEventListener("DOMContentLoaded", () => {
    const menuButton = document.querySelector(
        ".site-header__menu-toggle"
    );

    const navigation = document.querySelector(
        ".site-header__navigation"
    );

    if (!menuButton || !navigation) {
        return;
    }

    function closeMenu() {
        menuButton.setAttribute("aria-expanded", "false");
        menuButton.setAttribute(
            "aria-label",
            "Abrir menu de navegação"
        );

        navigation.classList.remove("is-open");
    }

    function toggleMenu() {
        const isExpanded =
            menuButton.getAttribute("aria-expanded") === "true";

        menuButton.setAttribute(
            "aria-expanded",
            String(!isExpanded)
        );

        menuButton.setAttribute(
            "aria-label",
            isExpanded
                ? "Abrir menu de navegação"
                : "Fechar menu de navegação"
        );

        navigation.classList.toggle("is-open");
    }

    menuButton.addEventListener("click", toggleMenu);

    navigation.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", closeMenu);
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeMenu();
        }
    });
});
