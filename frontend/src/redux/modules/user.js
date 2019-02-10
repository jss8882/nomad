//we will implement user's reduce in here

// imports

//actions

//action creator

//initial state

const initialState= {
    //localstorage는 브라우저에 저장하는 쿠키같은것 
    //JWT아이템이 유저 리듀서에 있는지를 체크하고 없으면 false값을 보낼것임 
    //만약 유저의 토큰이 localStorage에 존재한다면 로그인이되어있다는 의미임 그럼 true
    isLoggedIn: localStorage.getItem('jwt') || false
};


//reducer

function reducer(state = initialState, action){
    switch(action.type){
        default:
            return state;

    }
}

//reducer function

//exports

//reducer export

export default reducer;