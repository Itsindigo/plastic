import React, { Component } from 'react';
import { Link, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store';
import { Profile, Header, Footer } from './components';
import './styles/App.css';



class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <div className="App">
                    <Header />
                    <nav>
                        <Link to='/profile'>Profile</Link>
                    </nav>
                    <div className='wrapper'>
                        <Route path='/profile' component={Profile} />
                        <div className='push'></div>
                    </div>
                    <Footer />
                </div>
            </Provider>
        );
    }
}

export default App;





