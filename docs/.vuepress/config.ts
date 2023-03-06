import { defineUserConfig } from 'vuepress'
import { recoTheme } from 'vuepress-theme-reco'



export default defineUserConfig({
  base: "/~chenxman/",

  locales: {
    "/": {
      lang: "zh-CN",
      title: "小满の主页",
      description: '课程主页',
      // 设置favicon
      // head: [['link', { rel: 'icon', href: '/llx.jpg' }]],
    },
  },


})