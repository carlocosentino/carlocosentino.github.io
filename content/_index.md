---
title: ''
summary: ''
date: 2026-05-25
type: landing

sections:
  - block: resume-biography-3
    content:
      username: me
      text: ''
      button:
        text: Currículo Lattes
        url: http://lattes.cnpq.br/9403069473693221
      headings:
        about: 'Sobre'
        education: 'Formação'
        interests: 'Linhas de pesquisa'
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle
  - block: markdown
    content:
      title: 'Hub científico'
      subtitle: ''
      text: |-
        Página agregadora da produção científica e da atuação acadêmica de Carlo Cosentino. Reúne publicações, linhas de pesquisa, anúncios e remissões aos demais canais científicos – ORCID, Google Scholar, Currículo Lattes, Academia.edu, ResearchGate e SIGAA/UFPE.

        A produção advocatícia e a atuação profissional como sócio do escritório Cosmo e Cosentino Advogados encontram-se no sítio institucional próprio, em [www.cosmocosentino.com](https://www.cosmocosentino.com), e no hub público [linktr.ee/carlocosentino](https://linktr.ee/carlocosentino).
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
    content:
      title: Publicações recentes
      text: ''
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      view: citation
  - block: collection
    id: news
    content:
      title: Notícias
      subtitle: ''
      text: ''
      page_type: blog
      count: 5
      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      offset: 0
      order: desc
    design:
      view: card
      spacing:
        padding: [0, 0, 0, 0]
---
