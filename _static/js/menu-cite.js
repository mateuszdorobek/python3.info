let today = new Date()
let year = today.getFullYear()
let datetime = today.toISOString()
let date = datetime.split('T')[0]
let url = window.location.href
let revision = $('footer span.commit code').text()
let chapter = $('div[itemprop="articleBody"] h1').text()

const CITATION = `<div id="cite" itemscope itemtype="http://schema.org/ScholarlyArticle">
    <label for="citation">Cite this page:</label>
    <blockquote itemprop="citation" id="citation">
    
        <!-- author -->
        <span itemprop="author" itemscope itemtype="http://schema.org/Person">
            <link itemprop="url" href="https://orcid.org/0000-0002-2961-0617" />
            <span itemprop="name"><span itemprop="familyName">Harasymczuk</span>, <span itemprop="givenName">Matt</span></span>
        </span>.
        
        <!-- title -->    
        <cite itemprop="headline">Python: from None to Machine Learning.</cite>
        
        <!-- chapter -->
        <span itemscope itemtype="https://schema.org/Chapter" >
            <span itemprop="name">${chapter}</span>
             <link itemprop="isPartOf" itemscope itemtype="https://schema.org/Book" itemid="https://python.astrotech.io" />
        <span>
        
        <!-- year -->
        (<time itemprop="datePublished" datetime="${datetime}">${year}</time>)
        
        <!-- publisher -->
        <span itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
            <span itemprop="name">Analog Astronaut Training Center</span>.
        </span>
        
        <!-- version -->
        ISBN: <span itemprop="isbn">978-83-957186-2-5</span>.
        Revision: <span itemprop="version">${revision}</span>.
        
        <!-- url -->
        Retrived: <time itemprop="dateModified" datetime="${datetime}">${date}</time>.
        URL: <a itemprop="url" href="${url}">${url}</a>
        
        <!-- license -->
        License: <a itemprop="license" rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">License CC-BY-SA-4.0</a>
    </blockquote>`;


document.addEventListener("DOMContentLoaded", () => {
    // let left_menu = document.querySelectorAll('nav[class="wy-nav-side"]')[0];
    var left_menu = $('nav[class="wy-nav-side"]');
    left_menu.append(CITATION);
});
