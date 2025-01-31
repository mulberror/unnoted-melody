document.addEventListener('DOMContentLoaded', function() {
    const body = document.body;
    const html = document.documentElement;
    const homeProfile = document.querySelector('.home-profile');
    const scrollButton = document.getElementById('scrollButton');
    
    if (homeProfile) {
        body.classList.add('custom-background');
        updateBackground();
        setBodyBackgroundHeight();
        positionScrollButton();
    }

    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.attributeName === 'data-theme') {
                updateBackground();
            }
        });
    });

    observer.observe(html, { attributes: true });

    function updateBackground() {
        const theme = html.getAttribute('data-theme');
        const isRootPage = /^\/(en\/)?(page\/\d+\/)?$/.test(
          window.location.pathname
        );
        if (isRootPage) {
            if (theme === 'dark') {
                body.style.backgroundImage = 'url("/background-dark.webp")';
            } else {
                body.style.backgroundImage = 'url("/background-light.webp")';
            }
        } else {
            body.style.backgroundImage = ''; // 移除背景图片
        }
    }

    function setBodyBackgroundHeight() {
        const homeProfileHeight = homeProfile.offsetHeight;
        body.style.height = `${homeProfileHeight}px`;
        body.style.backgroundSize = `auto ${homeProfileHeight}px`;
    }

    function positionScrollButton() {
        const windowHeight = window.innerHeight;
        scrollButton.style.top = `${windowHeight * 0.8}px`; // 按钮位置在背景图片底部上方一点
        scrollButton.style.display = 'block';
    }

    const resizeObserver = new ResizeObserver(() => {
        setBodyBackgroundHeight();
        positionScrollButton();
    });
    resizeObserver.observe(homeProfile);

    scrollButton.addEventListener('click', function() {
        window.scrollTo({
            top: homeProfile.offsetHeight,
            behavior: 'smooth'
        });
    });

    const menuItems = document.querySelectorAll('.menu-item.has-children');

    menuItems.forEach(menuItem => {
        const dropdownIcon = menuItem.querySelector('.dropdown-icon');
        const subMenu = menuItem.querySelector('.sub-menu');

        if (dropdownIcon && subMenu) {
            let isHoveringMenuItem = false;
            let isHoveringSubMenu = false;

            menuItem.addEventListener('mouseenter', function() {
                isHoveringMenuItem = true;
                dropdownIcon.classList.add('rotate');
            });

            menuItem.addEventListener('mouseleave', function() {
                isHoveringMenuItem = false;
                setTimeout(() => {
                    if (!isHoveringSubMenu) {
                        dropdownIcon.classList.remove('rotate');
                    }
                }, 100);
            });

            subMenu.addEventListener('mouseenter', function() {
                isHoveringSubMenu = true;
            });

            subMenu.addEventListener('mouseleave', function() {
                isHoveringSubMenu = false;
                setTimeout(() => {
                    if (!isHoveringMenuItem) {
                        dropdownIcon.classList.remove('rotate');
                    }
                }, 300);
            });
        }
    });
});