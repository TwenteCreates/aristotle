import firebase from '@/services/firebase';
import { CREDENTIALS_LOGIN_PROVIDER, GOOGLE_LOGIN_PROVIDER, LINKEDIN_LOGIN_PROVIDER, FACEBOOK_LOGIN_PROVIDER } from './loginProviders';

const LOGIN = 'LOGIN';
const LOGIN_REQUEST = 'login_request';
const LOGIN_SUCCESS = 'login_success';
const LOGIN_ERROR = 'login_error';

const LOGOUT = 'logout';
const LOGOUT_REQUEST = 'logout_request';
const LOGOUT_SUCCESS = 'logout_success';
const LOGOUT_ERROR = 'logout_error';


export { LOGIN, LOGIN_SUCCESS, LOGOUT, LOGOUT_SUCCESS };

const state = () => ({
    profile: {},
    loggedIn: false,
    loginInProgress: false,
    logoutInProgress: false,
});

const mutations = {
    [LOGIN_REQUEST](state) {
        state.loggedIn = false;
        state.loginInProgress = true;
        state.profile = {};
    },
    [LOGIN_SUCCESS](state, authResult) {
        state.loggedIn = true;
        state.loginInProgress = false;
        state.profile = authResult;
    },
    [LOGIN_ERROR](state, error) {
        state.loggedIn = false;
        state.loginInProgress = false;
        state.profile = {};
    },
    [LOGOUT_REQUEST](state) {
        state.logoutInProgress = true;
    },
    [LOGOUT_SUCCESS](state) {
        state.loggedIn = false;
        state.logoutInProgress = false;
        state.profile = {};
    },
    [LOGOUT_ERROR](state, error) {
        state.logoutInProgress = false;
    },
};

const actions = {
    async [LOGIN]({ commit, state }, { provider, credentials }) {
        if (state.loggedIn)
            return;

        commit(LOGIN_REQUEST);

        try {
            let authResult;
            switch (provider) {
                case CREDENTIALS_LOGIN_PROVIDER:
                    authResult = await firebase.auth().signInWithEmailAndPassword(credentials.email, credentials.password);
                    break;
                case GOOGLE_LOGIN_PROVIDER:
                    authResult = await firebase.auth().signInWithPopup(new firebase.auth.GoogleAuthProvider());
                    break;
                default:
            }
        } catch (error) {
            alert(error)
            commit(LOGIN_ERROR, error);
        }
    },

    async [LOGOUT]({ commit }) {
        commit(LOGOUT_REQUEST);
        try {
            await firebase.auth().signOut();
            commit(LOGOUT_SUCCESS);
        } catch (error) {
            commit(LOGOUT_ERROR);
        }
    }
};

export default {
    state,
    mutations,
    actions
};
