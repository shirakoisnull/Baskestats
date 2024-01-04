<script>
 // import ConfirmationModal from "../ConfirmationModal.svelte";
  import { onMount } from "svelte";
  import { navigate } from "svelte-routing";

  // TODO: add player to championship association logic
//   let showModal = false;
//   let selectedPlayer = null;
  // Assuming championshipsData contains your championship entries, fetched from somewhere
  // Initialize championships as an empty array
  let championships = [];

  // Fetch championships data from the backend
  async function fetchChampionships() {
    try {
      const response = await fetch("http://127.0.0.1:5004/championships"); // Replace with your API endpoint
      if (response.ok) {
        const champData = await response.json();

        // Assuming the structure is [[championship_id, championship_name, championship_city, championship_wins, championship_losses], ...]
        championships = champData.map((champ) => ({
          cid: champ[0],
          year: champ[1],
        }));

        // championships array assumed to be an array of objects with specific properties for each championship
      } else {
        console.error("Failed to fetch championships:", response.status);
        // Handle error
      }
    } catch (error) {
      console.error("Error fetching championships:", error);
      // Handle error
    }
  }

  // Fetch player data on component mount
  onMount(fetchChampionships);

  function handleClick(event) {
    navigate("/newchamp");
  }

  async function deleteChamp(champ) {
    const confirmation = window.confirm(
      `Are you sure you want to delete championship #${champ.id}?`
    );
    if (confirmation) {
      try {
        const response = await fetch(`http://127.0.0.1:5004/championships/${champ.id}`, {
          method: "DELETE",
        });

        if (response.ok) {
          fetchChampionships();
          console.log("Championship deleted successfully!");
          alert(`Deleted ${champ.id}`);
          // Perform any necessary actions upon successful deletion
          // For example, update the UI or reload championship list
        } else {
          console.error("Failed to delete championship:", response.statusText);
        }
      } catch (error) {
        console.error("Error deleting championship:", error);
      }
    }
    // championshipsData = championshipsData.filter((t) => t.id !== championship.id);
  }
  function handleUpdate(champ) {
    navigate(`/editchamp`, { state: { champ } });
  }
  
  function handleDraw() {
    navigate('/draw');
  }

</script>

<div class="card">
<h1>Championship Management</h1>
  <button on:click={handleClick}>Create New Championship</button>
  <button on:click={handleDraw}>Draw Championship</button>
</div>

{#if championships.length === 0}
  <p>No championships found.</p>
{:else}
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Year</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {#each championships as champ}
      <tr>
        <td>{champ.cid}</td>
        <td>{champ.year}</td>
        <td>
          <button on:click={() => handleUpdate(champ)}>Update</button>
          <button class="delete-button" on:click={() => deleteChamp(champ)}>Delete</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>
{/if}
<button class="back-button" on:click={() => navigate("/secretary")}>Go Back</button>

<style>
  table {
    width: 50%;
    border-collapse: collapse;
    margin: auto; 
  }

  th,
  td {
    padding: 10px;
    border: 1px solid #ccc;
    text-align: center;
  }

  th {
    /* background-color: #f2f2f2; */
    font-weight: bold;
  }

  tr:hover {
    background-color: #e9e9e921;
  }

  /* Style for update and delete buttons */
  button {
    padding: 6px 10px;
    margin: 2px;
    cursor: pointer;
    color: white;
    /* border: none; */
    border-radius: 4px;
  }

   /* Style the back button */
   .back-button {
    position: absolute;
    top: 20px;
    left: 20px;
    padding: 10px;
    background-color: #ff4000;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

</style>
