import React,{Component} from "react";
import Auth from "./presenter";

//컨테이너를 클래스로 만듬 이는 State를 가지는 컴포넌트라는 의미임.
class Container extends Component{
    // 기본 state
    state={
        action:"login"
    };

    render(){
        const {action} = this.state;
        return <Auth action={action} changeAction={this._changeAction}/>
    }

    _changeAction = () => {
        //setState를 사용하면 state를 변경할수 있음
        this.setState( 
            prevState =>{
                //중괄호를 사용하는 것은 패턴매치잉ㅁ
                // const action = prevState.action과 동일한 기능을 한다
                const {action} = prevState;
                if(action==='login'){
                    return{
                        action:"signup"
                    };
                }
                else if (action==='signup'){
                    return{
                        action:"login"
                    };
                }

            }

        );

    }
}

export default Container;