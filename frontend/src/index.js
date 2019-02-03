import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import store from './redux/configureStore';
import './index.css';
import App from './App';

console.log(store.getState());

ReactDOM.render(
    // 합친 리듀서의 store를 불러옴
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root')
);
