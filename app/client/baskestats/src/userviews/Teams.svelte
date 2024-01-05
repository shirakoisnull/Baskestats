<script>
  import { fetchTeams } from "../api.js";
  import { onMount } from "svelte";

  let teams = [];

  onMount(async () => {teams = await fetchTeams();});

</script>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>City</th>
      <th>Wins</th>
      <th>Losses</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {#each teams as team}
      <tr>
        <td>{team[1]}</td>
        <td>{team[2]}</td>
        <td>{team[3]}</td>
        <td>{team[4]}</td>
        <td>
            <button>Info</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>