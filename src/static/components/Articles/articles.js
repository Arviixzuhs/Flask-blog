class Articles extends HTMLElement {
  connectedCallback() {
    this.articles = []

    this.innerHTML = `
      <div class="searchBarContainer">
        <input type="text" id="searchArticle" class="searchBar" placeholder="Buscar por título...">
        <i class='bx bx-search icon'></i>
      </div>
      <div class="articles"></div>
    `

    this.setupSearch()
    this.fetchArticles()
  }

  async fetchArticles() {
    try {
      const response = await fetch('/articles')
      if (!response.ok) {
        throw new Error('Error al obtener los artículos')
      }
      this.articles = await response.json()
      this.renderArticles(this.articles)
    } catch (error) {
      console.error('Error:', error)
    }
  }

  setupSearch() {
    const input = this.querySelector('#searchArticle')
    if (input) {
      input.addEventListener('input', (e) => {
        const searchValue = e.target.value.toLowerCase()
        const filteredArticles = this.articles.filter(
          (article) =>
            article.title.toLowerCase().includes(searchValue) ||
            article.tags.split(',').some((key) => key.toLowerCase().includes(searchValue))
        )
        this.renderArticles(filteredArticles)
      })
    }
  }

  renderArticles(articles) {
    const articlesContainer = this.querySelector('.articles')
    articlesContainer.innerHTML = articles
      .map(
        (item) => `
      <article class="articleCard">
        <img src="${item.image}" alt="${item.title}" class="articleCardImg" />
        <div class="articleCardContent">
          <div class="articleCardBody">
            <h3>${item.title}</h3>
            <p>${item.description}</p>
          </div>
          <div class="articleCardFooter">
            ${item.tags
              .split(',')
              .map((key) => `<span class="articleCardKey">${key}</span>`)
              .join('')}
          </div>
        </div>
      </article>
    `
      )
      .join('')
  }
}

customElements.define('articles-component', Articles)
