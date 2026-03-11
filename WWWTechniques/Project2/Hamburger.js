const mq = window.matchMedia("(max-width: 800px)");

function handleWidthChange(e) {
  if (e.matches) {
    // The media query now matches
    ShowMenu(true);
  } else {
    // It no longer matches
    ShowMenu(true);
  }
}

handleWidthChange(mq);

mq.addEventListener("change", handleWidthChange);

function ToggleMenu() {
    const isVisible = document.querySelector('.MenuButton').style.display === 'flex';
    ShowMenu(!isVisible);
}

function ShowMenu(visible) {
    console.log("Showing menu: " + visible);
    const menu = document.querySelectorAll('.MenuButton');
    menu.forEach(item => {
        item.style.display = visible ? 'flex' : 'none';
    });
}