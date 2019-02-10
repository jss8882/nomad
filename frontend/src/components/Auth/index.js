//authorization 컴포넌트를 Redux Store와 연결해 주어야함 
import {connect} from "react-redux";
import Container from "./container";



export default connect()(Container);