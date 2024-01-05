<script>
  import { fetchPlayers } from "../api.js";
  import { onMount } from "svelte";

  let players = [];

  onMount(async () => {players = await fetchPlayers();});

    function handleView(player){

    }

</script>

<table>
  <thead>
    <tr>
        <!-- NA EXEI ICON ME FATSOULA OR SOMETHING -->
      <th>Name</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {#each players as player}
      <tr>
        <td>{player[1]}</td>
        <td>
            <button>Info</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>