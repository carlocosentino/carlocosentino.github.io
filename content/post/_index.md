---
title: 'Notícias'
date: 2026-06-04
type: landing

sections:
  - block: markdown
    content:
      title: 'Notícias'
      text: |-
        Novidades, lançamentos e registros da produção acadêmica e da atuação de Carlo Cosentino.
    design:
      columns: '1'
  - block: collection
    id: noticias
    content:
      count: 0
      sort_by: Date
      order: desc
      filters:
        folders:
          - post
        featured_only: false
    design:
      view: article-grid
      columns: 2
---
