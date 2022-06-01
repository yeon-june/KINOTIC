// import router from '@/router'
import axios from 'axios'
import drf from '@/api/index.js'


export default {


  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: localStorage.getItem('currentUser') || '',
    profile: {},
    authError: null,
    admins : ['yj', 'minsung', 'yeonn']
  },

  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    admins : state => state.admins
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error
  },

  actions: {
    // 팔로우
    followUser({getters, commit}, userPk){
      axios({
        url: drf.accounts.follow(userPk),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(
        res=> {commit('SET_PROFILE', JSON.parse(JSON.stringify(res.data)))
        this.$router.push({name:'profile', params:{userPk}})})
      .catch(err => console.error(err.response))
    },

    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    removeCurrent({ commit }) {
      commit('SET_CURRENT_USER', '')
      localStorage.setItem('currentUser', '')
    },

    login({ commit, dispatch }, credentials) {

      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          if (document.referrer == 'http://localhost:8080/signup') {
            document.location.href = "/"
          } else {
            history.go(-1)
          }
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    signup({ commit }, credentials) {

      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then(() => {
          alert('성공적으로 회원가입이 완료되었습니다')
          commit('SET_AUTH_ERROR', null)
          document.location.href = "/login"
          
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    logout({ getters, dispatch }) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        data: {},
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          dispatch('removeCurrent')
          alert('성공적으로 logout!')
          document.location.href = "/"
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_CURRENT_USER', res.data)
            localStorage.setItem('currentUser', res.data.username)  
          })
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              document.location.href="/login"
            }
          })
      }
    },

    fetchProfile({ commit }, { username }) {
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
      })
        .then(res => {
          commit('SET_PROFILE', JSON.parse(JSON.stringify(res.data)))
        })
    },
  },
}
