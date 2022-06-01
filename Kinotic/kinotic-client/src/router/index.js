import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignupView from '@/views/SignupView.vue'
import LoginView from '@/views/LoginView.vue'
import ExploreView from '@/views/ExploreView.vue'
import RecommendView from '@/views/RecommendView.vue'
import CommunityView from '@/views/CommunityView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleNewView from '@/views/ArticleNewView'
import ArticleEditView from '@/views/ArticleEditView'
import MypageView from '@/views/MypageView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SearchView from '@/views/SearchView.vue'

import LogoutView from '@/views/LogoutView.vue'
import NotFound404 from '@/views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {//홈_nav
    path: '', //=> http://localhost:8080
    name: 'home',
    component: HomeView
  },
  {//회원가입
    path: '/signup', //=> http://localhost:8080/signup
    name: 'signup',
    component: SignupView
  },
  {//로그인
    path: '/login', //=> http://localhost:8080/login
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {//탐색_nav
    path: '/explore', //=> http://localhost:8080/explore
    name: 'explore',
    component: ExploreView
  },
  {//탐색_nav
    path: '/search/:search', //=> http://localhost:8080/explore
    name: 'search',
    component: SearchView,
  },
  {//추천_nav
    path: '/recommend', //=> http://localhost:8080/recommend
    name: 'recommend',
    component: RecommendView
  },
  {//찜 목록_nav
    path: '/community', //=> http://localhost:8080/community
    name: 'community',
    component: CommunityView
  },  
  {
    path: '/articles/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/articles/:articlePk',
    name: 'article',
    component: ArticleDetailView
  },
  {
    path: '/articles/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {//마이페이지_nav
    path: '/profile/:username',  // /profile/neo
    name: 'profile',
    component: ProfileView
  },
    {//마이페이지_nav
      path: '/mypage/:username',  // /profile/neo
      name: 'mypage',
      component: MypageView
    },
  //영화 페이지
  {
    path: '/movies/:moviePk',
    name: 'movie',
    component: MovieDetailView
  },
  //에러처리
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
