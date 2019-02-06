import Reactotron from "reactotron-react-js";
import { reactotronRedux } from "reactotron-redux";

//use함수를 사용하여 플러그인추가
Reactotron.configure({name:"nomadgram"})
.use(reactotronRedux())
.connect();

export default Reactotron;