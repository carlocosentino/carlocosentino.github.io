---
title: 'Notícias'
date: 2026-06-04
aliases:
  - /posts/
  - /events/
type: landing

sections:
  - block: markdown
    content:
      title: 'Notícias'
      text: |-
        <style>
        .page-body section.hbb-section{padding-top:3.6rem!important;padding-bottom:.3rem!important}
        .page-body section.hbb-section+section.hbb-section{padding-top:.3rem!important}
        .page-body section.hbb-section .flex.flex-col.gap-3{gap:.15rem!important}
        .page-body section.hbb-section p{margin-top:0!important;margin-bottom:.2rem!important}
        </style>
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
