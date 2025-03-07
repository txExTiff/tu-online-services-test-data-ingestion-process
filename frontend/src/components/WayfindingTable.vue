<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

// Store data
const data = ref([]);

// Messages
const message = ref("");
const messageType = ref(""); // "success" or "error"

// Function to show message and fade out after 3 seconds
const showMessage = (msg, type) => {
  message.value = msg;
  messageType.value = type;
  setTimeout(() => {
    message.value = ""; // Clear message after 3 seconds
  }, 3000);
};

// Fetch data function
const fetchData = async () => {
  try {
    const response = await axios.get("http://localhost:8072/wayfinding-directory");
    data.value = response.data;
    showMessage("Data loaded successfully!", "success");
  } catch (error) {
    showMessage("Error fetching data!", "error");
  }
};

// Sync data function
const syncData = async () => {
  try {
    await axios.post("http://localhost:8072/sync-wayfinding");
    showMessage("Data successfully synced!", "success");
    fetchData();
  } catch (error) {
    showMessage("Error syncing data!", "error");
  }
};

// Fetch data when component mounts
onMounted(fetchData);
</script>

<template>
  <div>
    <h2>Wayfinding Directory Data Ingestion</h2>

    <button @click="syncData">Sync Data</button>

    <!-- Success / Error Message (Under Button) -->
    <p v-if="message" :class="['message', messageType]">{{ message }}</p>

    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Office Location</th>
          <th>Phone</th>
          <th>Room</th>
          <th>Department</th>
          <th>Last Modified</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="entry in data" :key="entry.id">
          <td>{{ entry.name }}</td>
          <td>{{ entry.office_location }}</td>
          <td>{{ entry.telephone_number }}</td>
          <td>{{ entry.room_number }}</td>
          <td>{{ entry.department }}</td>
          <td>{{ entry.last_modified }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
h2 {
  text-align: center;
  margin-bottom: 1rem;
}

button {
  display: block;
  margin: 1rem auto;
  padding: 10px 20px;
  font-size: 1rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #36976b;
}

/* Message Styling */
.message {
  text-align: center;
  font-size: 1rem;
  padding: 10px;
  border-radius: 5px;
  margin: 10px auto;
  width: 50%;
  transition: opacity 0.5s ease-in-out;
  opacity: 1;
}

.success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

/* Hide message when cleared */
.message:empty {
  opacity: 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

th, td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}

th {
  background-color: #42b983;
  color: white;
}
</style>
