---
title: ''
summary: ''
date: 2026-05-25
type: landing

sections:
  - block: markdown
    content:
      text: |
        <style>
        .hero{position:relative;left:50%;transform:translateX(-50%);width:min(1140px,92vw);display:grid;grid-template-columns:minmax(330px,470px) minmax(0,1fr);gap:2.5rem;align-items:center;min-height:78vh}
        .hero__photo{position:relative;display:flex;align-items:center;justify-content:center}
        .hero__photo img{width:100%;max-height:84vh;object-fit:contain;display:block;-webkit-mask-image:radial-gradient(130% 118% at 50% 46%,#000 46%,rgba(0,0,0,.5) 72%,transparent 97%);mask-image:radial-gradient(130% 118% at 50% 46%,#000 46%,rgba(0,0,0,.5) 72%,transparent 97%)}
        .hero__info{color:#e8e8ea}
        .hero__kicker{letter-spacing:.2em;font-size:.72rem;text-transform:uppercase;color:#8aa0b4;font-weight:600}
        .hero__name{font-size:clamp(1.7rem,3vw,2.5rem);font-weight:700;line-height:1.05;margin:.2rem 0 .35rem;letter-spacing:-.01em}
        .hero__role{font-size:.92rem;color:#aebccb;font-weight:600;margin-bottom:.85rem}
        .hero__bio{font-size:.95rem;line-height:1.6;color:#c9ced6;max-width:42ch}
        .hero__btn{display:inline-block;margin-top:1.1rem;padding:.58rem 1.15rem;border:1px solid #2c3340;border-radius:10px;color:#e8e8ea;text-decoration:none;font-weight:600;font-size:.9rem;transition:background .2s}
        .hero__btn:hover{background:#161a22}
        .hero__social{display:flex;gap:1rem;margin-top:1.2rem;flex-wrap:wrap}
        .hero__social a{color:#8aa0b4;text-decoration:none;font-size:.84rem;font-weight:500}
        .hero__social a:hover{color:#e8e8ea}
        @media(max-width:900px){.hero{grid-template-columns:1fr;text-align:center;min-height:auto;gap:1rem;padding-top:.5rem}.hero__photo{max-width:400px;margin:0 auto;background:none}.hero__photo img{height:auto;max-height:64vh;-webkit-mask-image:radial-gradient(135% 118% at 50% 42%,#000 60%,transparent 100%);mask-image:radial-gradient(135% 118% at 50% 42%,#000 60%,transparent 100%)}.hero__name{font-size:clamp(2rem,8vw,2.6rem)}.hero__bio{margin:0 auto;font-size:1rem}.hero__social{justify-content:center}}
        </style>
        <div class="hero">
          <div class="hero__photo"><img src="/img/carlo-portrait.jpg" alt="Carlo Cosentino"></div>
          <div class="hero__info">
            <div class="hero__kicker">Hub científico</div>
            <h1 class="hero__name">Carlo Cosentino</h1>
            <div class="hero__role">Professor Adjunto · Faculdade de Direito do Recife · UFPE</div>
            <p class="hero__bio">Doutor em Direito pela UFPE. Pesquisa os impactos das tecnologias da informação e da comunicação nas relações de trabalho — da plataformização ao neotaylorismo digital, em diálogo com a teoria social crítica.</p>
            <a class="hero__btn" href="/sobre/">Saiba mais →</a>
            <div class="hero__social">
              <a href="mailto:contato@carlocosentino.com.br">Contato</a>
              <a href="https://orcid.org/0000-0002-7661-4688" target="_blank" rel="noopener">ORCID</a>
              <a href="https://scholar.google.com/citations?user=8O4wNSUAAAAJ" target="_blank" rel="noopener">Google Scholar</a>
              <a href="http://lattes.cnpq.br/9403069473693221" target="_blank" rel="noopener">Lattes</a>
              <a href="https://ufpe.academia.edu/CarloCosentino" target="_blank" rel="noopener">Academia.edu</a>
              <a href="https://www.researchgate.net/profile/Carlo-Cosentino-3" target="_blank" rel="noopener">ResearchGate</a>
            </div>
          </div>
        </div>
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Publicações em destaque
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: article-grid
      columns: 2
  - block: collection
    id: news
    content:
      title: Notícias
      count: 5
      filters:
        folders:
          - post
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      offset: 0
      order: desc
    design:
      view: card
  - block: markdown
    content:
      title: 'Advocacia'
      text: |-
        Além da atuação acadêmica, Carlo Cosentino é advogado (OAB/PE 22.955) e sócio do escritório **Cosmo e Cosentino Advogados**, com atuação consultiva e contenciosa em Direito do Trabalho, Direito Sindical e Terceiro Setor.

        [Conheça o escritório →](https://www.cosmocosentino.com)
    design:
      columns: '1'
---
