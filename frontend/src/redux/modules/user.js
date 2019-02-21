//we will implement user's reduce in here

// imports

//actions
const SAVE_TOKEN = "SAVE_TOKEN";
//action creator
function saveToken(token) {
  return {
    type: SAVE_TOKEN,
    token
  };
}
//API actions

function facebookLogin(access_token) {
  return function(dispatch) {
    fetch("/users/login/facebook/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        access_token
      })
    })
      .then(response => response.json())
      .then(json => console.log(json))
      .catch(err => console.log(err));
  };
}
function usernameLogin(username, password) {
  return function(dispatch) {
    fetch("/rest-auth/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username,
        password
      })
    })
      .then(response => response.json())
      .then(json => {
        if (json.token) {
          dispatch(saveToken(json.token));
        }
      })
      .catch(err => console.log(err));
  };
}

//initial state

const initialState = {
  //localstorage는 브라우저에 저장하는 쿠키같은것
  //JWT아이템이 유저 리듀서에 있는지를 체크하고 없으면 false값을 보낼것임
  //만약 유저의 토큰이 localStorage에 존재한다면 로그인이되어있다는 의미임 그럼 true
  isLoggedIn: localStorage.getItem("jwt") ? true : false
};

//reducer

function reducer(state = initialState, action) {
  switch (action.type) {
    case SAVE_TOKEN:
      return applySetToken(state, action);
    default:
      return state;
  }
}

//reducer function
function applySetToken(state, action) {
  const { token } = action;
  console.log("hello")
  console.log(token);
  localStorage.setItem("jwt", token);
  return {
    ...state,
    isLoggedIn: true,
    token: token
  };
}

//exports
const actionCreators = {
  facebookLogin,
  usernameLogin
};
export { actionCreators };

//reducer export

export default reducer;
