import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    toekn:'',
    user: {
      id: 0,
      username: '',
    },
    team: {
      id:0,
      name: '',
      plan: '',
      max_leads: 0,
      max_clients: 0
    }
  },
  mutations: {
    initializeStore(state) {
      if(localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.username = localStorage.getItem('username')
        state.user.id = localStorage.getItem('userid')

        state.team.name = localStorage.getItem('team_name')
        state.team.id = localStorage.getItem('team_id')

        state.team.plan = localStorage.getItem('team_plan')
        state.team.max_leads = localStorage.getItem('team_max_leads')
        state.team.max_clients = localStorage.getItem('team_max_clients')
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user.id = 0 
        state.user.username = ''
        
        state.team.id = 0
        state.team.name = ''
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state, token) {
      state.token = ''
      state.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
    },
    setTeam(state, team) {
      state.team = team
      localStorage.setItem('team_id', team.id) 
      localStorage.setItem('team_name', team.name) 
    },
  },
  actions: {
  },
  modules: {
  }
})
