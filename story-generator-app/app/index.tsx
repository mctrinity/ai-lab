import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  Button,
  ScrollView,
  StyleSheet,
  Keyboard,
  Platform,
  KeyboardAvoidingView,
} from 'react-native';
import { Picker } from '@react-native-picker/picker';
import { useNavigation } from 'expo-router';

export default function HomeScreen() {
  const [prompt, setPrompt] = useState('');
  const [genre, setGenre] = useState('sci-fi');
  const [story, setStory] = useState('');
  const [loading, setLoading] = useState(false);

  const navigation = useNavigation();
  useEffect(() => {
    navigation.setOptions?.({ headerShown: false });
  }, [navigation]);

  const generateStory = async () => {
    Keyboard.dismiss();
    setLoading(true);
    try {
      const response = await fetch('http://192.168.1.108:8010/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, genre }),
      });
      const data = await response.json();
      setStory(data.story);
    } catch (err) {
      setStory('Failed to fetch story. Make sure the server is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <KeyboardAvoidingView
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      style={{ flex: 1 }}
      keyboardVerticalOffset={Platform.OS === 'ios' ? 60 : 0}
    >
      <ScrollView contentContainerStyle={styles.container} keyboardShouldPersistTaps="handled">
        <Text style={styles.title}>📝 AI Story Generator</Text>

        <Text style={styles.label}>Select a Genre</Text>
        <View style={styles.pickerWrapperWithLabel}>
          <Picker
            selectedValue={genre}
            onValueChange={(itemValue) => setGenre(itemValue)}
            mode={Platform.OS === 'android' ? 'dropdown' : undefined}
            style={styles.pickerField}
            itemStyle={Platform.OS === 'ios' ? styles.pickerItemIOS : {}}
          >
            <Picker.Item label="Sci-Fi" value="sci-fi" />
            <Picker.Item label="Fantasy" value="fantasy" />
            <Picker.Item label="Horror" value="horror" />
            <Picker.Item label="Romance" value="romance" />
            <Picker.Item label="Mystery" value="mystery" />
          </Picker>
        </View>

        <Text style={styles.label}>Prompt</Text>
        <TextInput
          style={[styles.input, { height: 100 }]}
          multiline
          textAlignVertical="top"
          value={prompt}
          onChangeText={setPrompt}
          placeholder="Describe your story idea..."
        />

        <Button title={loading ? 'Generating...' : 'Generate Story'} onPress={generateStory} disabled={loading} />

        <View style={styles.storyBox}>
          <Text style={styles.storyText}>{story}</Text>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: '#fff',
    flexGrow: 1,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginTop: 60,
    marginBottom: 10,
    textAlign: 'center',
  },
  label: {
    marginTop: 10,
    fontWeight: '600',
  },
  input: {
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 6,
    padding: 10,
    marginTop: 5,
    marginBottom: 10,
    backgroundColor: '#fff',
  },
  pickerWrapperWithLabel: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 6,
    backgroundColor: '#fff',
    marginTop: 5,
    marginBottom: 15,
    paddingHorizontal: 10,
    height: 50,
    justifyContent: 'center',
  },
  pickerField: {
    height: 50,
    width: '100%',
    justifyContent: 'center',
    color: '#000', // ✅ Ensures selected text is visible
    backgroundColor: '#fff',
  },
  pickerItemIOS: {
    height: 44,
    fontSize: 16,
    color: '#000', // ✅ Ensures dropdown items are readable
  },
  storyBox: {
    marginTop: 20,
    borderColor: '#eee',
    borderWidth: 1,
    padding: 15,
    borderRadius: 6,
    backgroundColor: '#fafafa',
    flexGrow: 1,
  },
  storyText: {
    fontSize: 16,
    lineHeight: 22,
  },
});
