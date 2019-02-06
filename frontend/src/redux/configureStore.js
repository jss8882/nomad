//configureStore에서 스토어를 설정하고 구성할것임 빼
import  { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from "redux-thunk"
//지금 버저에서 사용하지 않음
//import { routerReducer, routerMiddleware} from "react-router-redux";
import { connectRouter } from 'connected-react-router'
import { routerMiddleware } from 'connected-react-router'
import { createBrowserHistory } from 'history'
//import createHistory from "history/createBrowserHistory";
import { composeWithDevTools } from "redux-devtools-extension";
import { i18nState } from "redux-i18n";
import users from 'redux/modules/users'
import Reactotron from "ReactotronConfig"

const history = createBrowserHistory()

//글로벌한 미들웨어
//routerMiddleware는 리액트 라우터 리덕스인데 우리가 방금 생성한 히스토리와 싱크를 하기 위하여 사용
const middleware = [thunk,routerMiddleware(history)];


//node js의 전체 정보를 갖고 있는 변수임 
//이것이 prod / dev인지 알려줌
// prod / dev에 따라 스토어가 달라진다 
const env = process.env.NODE_ENV;
console.log(env)

if(env==="development"){
    //환경이 developoment일 때만 logger를 사용
    //production에서는 가볍게 하기 위함
    const { logger } = require("redux-logger")
    //미들웨어 배열에 logger도 추가.
    middleware.push(logger);

}



//여기에서 여러 리듀서들을 합칠것임
const reducer = combineReducers({
    users,
    router: connectRouter(history),
    //i18n을 위한 리듀서를 추가
    i18nState,
});


let store;

if(env==="development"){
    //reactotron를 위한 Store생성
    store = initialState =>
        Reactotron.createStore(
            reducer,
            composeWithDevTools(applyMiddleware(...middleware)));
} else{
    //...middleware를 사용하면 배열을 풀수 있다.
    //ex) ([1,2,3,4])배열을 (1,2,3,4)로 풀어줌
    //createStore의 두번쨰 인자로 미들웨어를 넣어준다, 
    //미들웨어를 적용하기 위하여 applyMiddleware함ㅁ수를 사용하고 그안에 미들웨어들을 넣음
    store = initialState =>
        createStore(reducer,applyMiddleware(...middleware));
}



//라우터를 생성할때 히스토리 오브젝트가 필요함 
export { history };

export default store();