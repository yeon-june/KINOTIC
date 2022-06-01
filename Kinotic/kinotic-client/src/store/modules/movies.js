import router from '@/router'
import axios from 'axios'
import drf from '@/api/index.js'

export default {  
state: {
  boxOffice: [],
  basicRec: [],
  weatherRec: [],
  userFollowRec: [],
  userLikeRec:[],
  movies: [],
  movies20: [],
  movie: {},
  movieTrailer: {},
  searches: [],
},

getters: {
  movies: state => state.movies,
  movie: state => state.movie,
  basicRec: state => state.basicRec,
  weatherRec: state => state.weatherRec,
  userFollowRec: state => state.userFollowRec,
  userLikeRec: state => state.userLikeRec,
  boxOffice: state => state.boxOffice,
  searches: state=> state.searches,
  movieTrailer: state => state.movieTrailer

},

mutations: {
  SET_MOVIES: (state, movies) => state.movies = movies,
  SET_MOVIE: (state, movie) => state.movie = movie,
  SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.reviews = reviews),
  SET_BASIC_REC: (state, basicRec) => state.basicRec = basicRec,
  SET_WEATHER_REC: (state, weatherRec) => state.weatherRec = weatherRec,
  SET_USERFOLLOW_REC: (state, userFollowRec) => state.userFollowRec = userFollowRec,
  SET_USERLIKE_REC: (state, userLikeRec) => state.userLikeRec = userLikeRec,
  SET_BOXOFFICE: (state, boxOffice) => state.boxOffice = boxOffice,
  SET_SEARCH: (state, searches) => state.searches = searches,
  SET_MOVIE_TRAILER: (state, movieTrailer) => state.movieTrailer = movieTrailer
},

actions: {
  fetchMovies({ commit }) {
    axios({
      url: drf.movies.movies(),
      method: 'get',
    })
      .then(res => {commit('SET_MOVIES', JSON.parse(JSON.stringify(res.data))) })
      .catch(err => console.error(err.response))
  },

  fetchMovie({ commit }, moviePk) {
    axios({
      url: drf.movies.movie(moviePk),
      method: 'get',
    })
      .then(res => commit('SET_MOVIE', JSON.parse(JSON.stringify(res.data))))
      .catch(err => {
        console.error(err.response)
        if (err.response.status === 404) {
          router.push({ name: 'NotFound404' })
        }
      })
  },

  //트레일러
  fetchMovieTrailer({ commit }, moviePk) {
    axios({
      url: drf.movies.movieTrailer(moviePk),
      method: 'get',
    })
      .then(res => commit('SET_MOVIE_TRAILER', JSON.parse(JSON.stringify(res.data))))
      .catch(err => {
        console.error(err.response)
        if (err.response.status === 404) {
          router.push({ name: 'NotFound404' })
        }
      })
  },

  // 검색 
  fetchSearch({ commit }, keyword) {
    axios({
      url: drf.movies.movieSearch(keyword),
      method: 'get',
    })
      .then(res => {commit('SET_SEARCH', JSON.parse(JSON.stringify(res.data))) })
      .catch(err => console.error(err.response))
  },

  //박스오피스 순위
  fetchBoxoffice({ commit }) {
    axios({
      url: drf.movies.movieBoxoffice(),
      method: 'get',
    })
      .then(res => {commit('SET_BOXOFFICE', JSON.parse(JSON.stringify(res.data))) })
      .catch(err => console.error(err.response))
  },
  //추천 받아오기
  fetchBasicRec({ commit }) {
    axios({
      url: drf.movies.movieRecBasic(),
      method: 'get',
    })
      .then(res => {commit('SET_BASIC_REC', JSON.parse(JSON.stringify(res.data))) })
      .catch(err => console.error(err.response))
  },

  fetchWeatherRec({ commit }) {
    axios({
      url: drf.movies.movieRecWeather(),
      method: 'get',
    })
      .then(res => {commit('SET_WEATHER_REC', JSON.parse(JSON.stringify(res.data))) })
      .catch(err => console.error(err.response))
  },

  fetchUserFollowRec({ commit, getters}) {
    axios({
      url: drf.movies.movieRecUserFollow(),
      method: 'get',
      headers: getters.authHeader,
    })
      .then(res => {commit('SET_USERFOLLOW_REC', JSON.parse(JSON.stringify(res.data))) })
      .catch(err => console.error(err.response))
  },

  
  fetchUserLikeRec({ commit, getters}) {
    axios({
      url: drf.movies.movieRecUserLike(),
      method: 'get',
      headers: getters.authHeader,
    })
      .then(res => {commit('SET_USERLIKE_REC', JSON.parse(JSON.stringify(res.data))) })
      .catch(err => console.error(err.response))
  },
  

  likeMovie({ commit, getters }, moviePk) {
    axios({
      url: drf.movies.likeMovie(moviePk),
      method: 'post',
      headers: getters.authHeader,
    })
      .then(res => commit('SET_MOVIE', JSON.parse(JSON.stringify(res.data))))
      .catch(err => console.error(err.response))
  },

  lookMovie({ commit, getters }, moviePk) {
    axios({
      url: drf.movies.lookMovie(moviePk),
      method: 'post',
      headers: getters.authHeader,
    })
      .then(res => commit('SET_MOVIE', JSON.parse(JSON.stringify(res.data))))
      .catch(err => console.error(err.response))
  },

  createReview({ commit, getters }, { moviePk, content }) {
    const review =  content 

    axios({
      url: drf.movies.movieReviews(moviePk),
      method: 'post',
      data: review,
      headers: getters.authHeader,
    })
      .then(res => {
        commit('SET_MOVIE_REVIEWS', JSON.parse(JSON.stringify(res.data)))
      })
      .catch(err => console.error(err.response))
  },

  updateReview({ commit, getters }, { moviePk, reviewPk, content }) {
    const review =  content 

    axios({
      url: drf.movies.movieReview(moviePk, reviewPk),
      method: 'put',
      data: review,
      headers: getters.authHeader,
    })
      .then(res => {
        commit('SET_MOVIE_REVIEWS', JSON.parse(JSON.stringify(res.data)))
      })
      .catch(err => console.error(err.response))
  },

  deleteReview({ commit, getters }, { moviePk, reviewPk}) {

      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.movies.movieReview(moviePk, reviewPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_MOVIE_REVIEWS', JSON.parse(JSON.stringify(res.data)))
          })
          .catch(err => console.error(err.response))
      }
  },

  rangeMovie({ commit }, rangetype){
    axios({
      url: drf.movies.movieRange(rangetype),
      method: 'get',
    })
      .then(res => {
        commit('SET_MOVIES', JSON.parse(JSON.stringify(res.data)))})
      .catch(err => console.error(err.response))
  },
},
}
