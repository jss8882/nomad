import { connect } from "react-redux";
import Container from "./container";

//state를 통해서 logged in prop를 컨테이너 컴포넌트로 보냄(./container.js)
const mapStateToProps = (state,ownProps) => {
  const { user } = state;
  return {
    isLoggedIn: user.isLoggedIn
  };
};


export default connect(mapStateToProps)(Container);