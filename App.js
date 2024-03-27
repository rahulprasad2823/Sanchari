import logo from './logo.svg';
import './App.css';
import Experience from './components/Experience'
import Bucketlist from './components/bucketlist';
import Popular from './components/popular';
import React, {useState, useEffect} from 'react';
import axios from 'axios';

function App() {

  return (
       <div class="main_container">
      <div class="header">
        <div class="left">
          <p>Sanchari</p>
        </div>
        <div class="right">
        <p><a href="#Experience">Experiences</a></p>
        <p><a href="#Popular">PopularPlaces</a></p>
        <p><a href="#Bucketlist">BucketList</a></p>
        </div>
      </div>
      <div class="floatingimage">
                <img src="https://images.unsplash.com/photo-1570304816841-906a17d7b067?q=80&w=3132&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" />
                <div class="overlay">
                    <p>Sanchari</p>
                    <h1 class="small">A Travel App</h1>
                </div>
        </div>
        <Experience />
        <Bucketlist />
        <Popular />
     </div>
  );
}

export default App;
