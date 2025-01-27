class Navbar extends HTMLElement {
  connectedCallback() {
    const currentPath = window.location.pathname

    this.innerHTML = `
      <header class="header">
        <link rel="stylesheet" href="${staticBaseUrl}components/Navbar/styles.css" />
        <nav class="preNavbar">
          <a href="/">Inicio</a>
          <div class="preNavbarIcons">
            <a href="https://github.com/arviixzuh" target="_blank">
              <i class='bx bxl-github icon'></i>
            </a>
            <a href="https://www.youtube.com/@Arviixzuh" target="_blank">
              <i class='bx bxl-youtube icon'></i>
            </a>
            <a href="https://twitter.com/Arviixzuh_" target="_blank">
              <i class='bx bxl-twitter icon'></i>
            </a>
          </div>
        </nav>
        <div class="blog">
          <img src="${staticBaseUrl}assets/arviixzuh.jpg" alt="" />
          <h3>Arviixzuh's Blog</h3>
        </div>
        <nav class="navbar">
          <a href="/list">Lista de Datos</a>
          <a href="/gallery">Galería</a>
          <a href="/video">Video</a>
          <a href="/audio">Audio</a>
          <a href="/drag">Drag and drop</a>
          <a href="/tictactoe">Tic Tac Toe</a>
          <a href="/admin" target="_blank">Administrar artículos</a>
        </nav>
      </header>
    `
    const links = this.querySelectorAll('.navbar a')
    links.forEach((link) => {
      if (link.getAttribute('href') === currentPath) {
        link.classList.add('active')
      }
    })
  }
}

customElements.define('navbar-component', Navbar)
