async function reloadPositions() {
    const response = await fetch(window.URLS.portfolio);
    const positions = await response.json();

    const portfolioRoot = document.getElementById('portfolio-container');
    for (const position of positions['positions']) {


        let addUrl = `/position/${position.id}/add/`
        let sellUrl = `/position/${position.id}/sell/`
        const divPortfolioRow = document.createElement('div');
        divPortfolioRow.classList.add('portfolio-row');
        divPortfolioRow.innerHTML = `
                <div class="portfolio-cell">${position.ticker_symbol}</div>
                <div class="portfolio-cell">${position.count}</div>
                <div class="portfolio-cell">${position.avg_price.toFixed(2)}</div>
                <div class="portfolio-cell">${position.price.toFixed(2)}</div>
                <div class="portfolio-cell">${position.current_price.toFixed(2)}</div>
                <div class="portfolio-cell">${position.change.toFixed(2)}%</div>
                <div class="portfolio-cell"><a href="${addUrl}">Add</a> / <a href="${sellUrl}">Sell</a></div>
                `
        portfolioRoot.appendChild(divPortfolioRow);

    }

    //portfolioRoot.innerHTML = '';
    const loader = document.getElementById('loader');
    loader.remove();
    const bottomRow = document.createElement('div')
    bottomRow.classList.add('portfolio-row')
    bottomRow.innerHTML = `
            <div class="portfolio-cell">Cash:</div>
            <div class="portfolio-cell"></div>
            <div class="portfolio-cell"></div>
            <div class="portfolio-cell">${positions.cash.toFixed(2)}</div>
            `
    portfolioRoot.appendChild(bottomRow)
}

reloadPositions()
