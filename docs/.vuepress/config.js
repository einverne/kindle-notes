const getConfig = require("vuepress-bar");
const { nav, sidebar } = getConfig();

module.exports = {
  title: 'EV 书摘',
  description: '这里包含我自己常用的读书软件中的书摘',
  plugins: [
    [
      "@vuepress/google-analytics",
      {
        ga: "G-S5CVEW25S9",
      },
    ],
    "@vuepress/back-to-top",
    "@vuepress/nprogress"
  ],
  markdown: {
    // markdown-it-anchor 的选项
    anchor: { permalink: false },
    // markdown-it-toc 的选项
    toc: { includeLevel: [1, 2] },
  },
  themeConfig: {
    lastUpdated: "上次更新",
    smoothScroll: true,
    nav: [
      {
        "text": "博客",
        "link": "https://blog.einverne.info"
      }
    ],
    sidebar
  }
}
