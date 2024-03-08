import React, { useState, useEffect } from 'react';
import { Text, View, Button, StyleSheet, FlatList, TextInput, Alert } from 'react-native';
import axios from 'axios';

export default function App() {
  const [books, setBooks] = useState([]);
  const [newBook, setNewBook] = useState({ title: '', author: '' });
  const [editingBook, setEditingBook] = useState(null);
  const [editedBook, setEditedBook] = useState({ title: '', author: '' });

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = () => {
    axios.get('https://cuddly-pancake-9774gppj96pg37q9w-5000.app.github.dev/books')
      .then(response => {
        setBooks(response.data.books);
      })
      .catch(error => {
        console.log(error.response);
      });
  };

  const addBook = () => {
    axios.post('https://cuddly-pancake-9774gppj96pg37q9w-5000.app.github.dev/books', newBook)
      .then(response => {
        setBooks(response.data.books);
        setNewBook({ title: '', author: '' });
      })
      .catch(error => {
        console.log(error.response);
      });
  };

  const deleteBook = (id) => {
    axios.delete(`https://cuddly-pancake-9774gppj96pg37q9w-5000.app.github.dev/books/${id}`)
      .then(response => {
        setBooks(response.data.books);
      })
      .catch(error => {
        console.log(error.response);
      });
  };

  const updateBook = () => {
    axios.put(`https://cuddly-pancake-9774gppj96pg37q9w-5000.app.github.dev/books/${editingBook.id}`, editedBook)
      .then(response => {
        setBooks(response.data.books);
        setEditingBook(null);
        setEditedBook({ title: '', author: '' });
      })
      .catch(error => {
        console.log(error.response);
      });
  };

  const renderItem = ({ item }) => (
    <View style={styles.item}>
      <Text>Title: {item.title}</Text>
      <Text>Author: {item.author}</Text>
      <Button title="Edit" onPress={() => setEditingBook(item)} />
      <Button title="Delete" onPress={() => deleteBook(item.id)} />
    </View>
  );

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        value={newBook.title}
        placeholder="Enter title"
        onChangeText={(text) => setNewBook({ ...newBook, title: text })}
      />
      <TextInput
        style={styles.input}
        value={newBook.author}
        placeholder="Enter author"
        onChangeText={(text) => setNewBook({ ...newBook, author: text })}
      />
      <Button title="Add Book" onPress={addBook} />
      
      {editingBook && (
        <View>
          <TextInput
            style={styles.input}
            value={editedBook.title}
            placeholder="Enter new title"
            onChangeText={(text) => setEditedBook({ ...editedBook, title: text })}
          />
          <TextInput
            style={styles.input}
            value={editedBook.author}
            placeholder="Enter new author"
            onChangeText={(text) => setEditedBook({ ...editedBook, author: text })}
          />
          <Button title="Update Book" onPress={updateBook} />
        </View>
      )}

      <FlatList
        data={books}
        renderItem={renderItem}
        keyExtractor={item => (item.id ? item.id.toString() : Math.random().toString())}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
  item: {
    borderBottomWidth: 1,
    borderBottomColor: 'gray',
    marginBottom: 10,
    paddingBottom: 10,
  },
});
