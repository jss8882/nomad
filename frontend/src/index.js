import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
//import { ConnectedRouter } from 'react-router-redux';
import { ConnectedRouter } from 'connected-react-router'
import store, { history } from 'redux/configureStore';
import App from "components/App"
import "ReactotronConfig";
import { translations } from "translations";
import I18n from "redux-i18n";
//reset css
import 'reset-css';


console.log(store.getState());

ReactDOM.render(
    // 합친 리듀서의 store를 불러옴
    <Provider store={store}>
        <ConnectedRouter history={history}>
        {/* I18n은 2개의 props를 가진다 첫번째는 번역파일: 번역파일을 불러온다, 또한 어플의 원래 언어를 가져옴
        또한 번역하려고 한 언어를 찾지 못했을때를 대비한 fallbackLang도 가진다
        이를 통하여 컴포넌트는 현재 언어를 체크할수 있게된다 */}
        <I18n translations={translations} initialLang="en" fallbackLang="en">
            <App />
        </I18n>
        </ConnectedRouter>
    </Provider>,
    document.getElementById('root')
);

//relative import, absolute import 라는것이 있음 
//파일을 디렉토리 처럼 복잡하지 않고, 모듈처럼 임포트를 하는 것이 보기에 편함
//그렇게 하기 위해서 프론트엔드 폴더에 .env라는 파일을 생성할것임
//.env파일 안에  NODE_PATH=src 를 추가하여 node에게 나의 모듈들이 src폴더 안에 있다는 것을 알려줌.