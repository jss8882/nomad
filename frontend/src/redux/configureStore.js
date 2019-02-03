//configureStore에서 스토어를 설정하고 구성할것임 빼

import  { createStore, combineReducers } from 'redux';
import users from './modules/users'

//여기에서 여러 리듀서들을 합칠것임
const reducer = combineReducers({
    users,
});

let store = initialState => createStore(reducer);

export default store();