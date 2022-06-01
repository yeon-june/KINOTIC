const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const ARTICLES = 'community/'
const COMMENTS = 'comments/'
const REVIEWS = 'reviews/'
const RECOMMEND = 'recommend/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
    // 팔로우
    follow: userpk => HOST + ACCOUNTS + userpk + '/follow/',

  },
  articles: {
    // /articles/
    articles: () => HOST + ARTICLES,
    // /articles/1/
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
  movies: {
    // movie 리스트 가져오기
    movies: () => HOST + MOVIES,
    // 디테일 movie/pk/
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    // trailer
    movieTrailer: moviePk => HOST + MOVIES + `${moviePk}/` + 'trailer/',

    // 영화 좋아요 누르기
    likeMovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'like/',
    // 본영화 표시
    lookMovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'look/',
    // 영화 리뷰 리스트
    movieReviews: moviePk => HOST + MOVIES + `${moviePk}/` + REVIEWS,
    // 리뷰 업데이트
    movieReview: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/`,

    // 영화추천 - 로그인 불필요
    // 날씨 기반 추천
    movieRecWeather: () => HOST + MOVIES + RECOMMEND + 'weather/',
    // 기본 영화 추천
    movieRecBasic: () => HOST + MOVIES + RECOMMEND + 'basic/',

    movieBoxoffice: () => HOST + MOVIES + 'boxoffice/',

    // 영화추천 - 로그인 필요
    // 팔로잉 기반 영화 추천
    movieRecUserFollow: () => HOST + MOVIES + RECOMMEND + 'following/',
    // 찜목록 기반 영화 추천
    movieRecUserLike: () =>  HOST + MOVIES + RECOMMEND + 'likemovie/',
    // 영화 검색
    movieSearch: (search) =>  HOST + MOVIES + `${search}/`,
    // 영화 정렬
    movieRange: (rangetype) => HOST + MOVIES + RECOMMEND + 'movieranges/' + `${rangetype}/`
  }
}
