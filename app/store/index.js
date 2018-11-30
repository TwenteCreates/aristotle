import Vuex from 'vuex'
import user from './user';

const createStore = () => {
    return new Vuex.Store({
        modules: {
            user,
        }
    })
}

export default createStore
