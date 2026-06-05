---
title: ''
summary: ''
date: 2026-05-25
type: landing

sections:
  - block: resume-biography
    content:
      username: me
      button:
        text: Saiba mais
        url: /sobre/
    design:
      background:
        gradient_mesh:
          enable: true
      avatar:
        size: xl
        shape: rounded
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
      subtitle: ''
      text: ''
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
      spacing:
        padding: [0, 0, 0, 0]
  - block: markdown
    content:
      title: 'Advocacia'
      text: |-
        Além da atuação acadêmica, Carlo Cosentino é advogado (OAB/PE 22.955) e sócio do escritório **Cosmo e Cosentino Advogados**, com atuação consultiva e contenciosa em Direito do Trabalho, Direito Sindical e Terceiro Setor.

        [Conheça o escritório →](https://www.cosmocosentino.com)
    design:
      columns: '1'
---
