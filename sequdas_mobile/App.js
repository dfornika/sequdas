import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { Header } from 'react-native-elements';

export default class App extends React.Component {
  render() {
      return (
	  <Header
	   leftComponent={{ icon: 'menu', color: '#fff' }}
	   centerComponent={{ text: 'SeqUDAS', style: { color: '#fff' } }}
	    />
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center'
  }
});
