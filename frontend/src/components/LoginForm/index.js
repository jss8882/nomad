import { connect } from "react-redux";
import Container from "./container";
import {actionCreators as userAction} from "redux/modules/user";

const mapDispatchToProps = (dispatch,ownProps) => {
    return {
        facebookLogin: (access_token)=>{
            dispatch(userAction.facebookLogin(access_token))
        },
        usernameLogin: (email,password)=>{
            dispatch(userAction.usernameLogin(email,password))
        }
    }
}

export default connect(null,mapDispatchToProps)(Container);