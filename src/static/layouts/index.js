class Layout extends HTMLElement {
  connectedCallback() {
    const slotContent = this.innerHTML

    this.innerHTML = `
      <main>
        <link href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css" rel="stylesheet" />
        <navbar-component></navbar-component>
        <section>
          <h3>${this.getAttribute('title') || 'Sin título'}</h3>
          <div class="content">
            ${slotContent}
          </div>
        </section>
      </main>
    `
  }
}

customElements.define('layout-component', Layout)
