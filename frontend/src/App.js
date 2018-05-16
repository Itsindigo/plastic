import React, { Component } from 'react';
import { Link, Route } from 'react-router-dom';

import './App.css';

const Profile = () => {
    return (
        <div>
            <h1>Hello my name is Matthew</h1>
        </div>
    )
};


class App extends Component {
    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1 className="App-title">Hello World!</h1>
                </header>
                <nav>
                    <Link to='/profile'>Profile</Link>
                </nav>
                <div>
                    <Route path='/profile' component={Profile} />
                </div>
            </div>
        );
    }
}

export default App;
