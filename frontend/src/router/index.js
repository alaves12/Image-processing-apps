import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Dehaze from '../views/Dehaze.vue'
import User from '../views/User.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { title: 'ページタイトル', desc: 'ディスクリプションを記述' }
  },
  {
    path: '/dehaze',
    name: 'Dehaze',
    component: Dehaze,
    meta: { title: 'ページタイトル', desc: 'ディスクリプションを記述' }
  },
  {
    path: '/user/:userId',
    name: 'user',
    component: User,
    meta: { title: 'ページタイトル', desc: 'ディスクリプションを記述' }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
