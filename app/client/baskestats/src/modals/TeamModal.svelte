<script>
  export let showModal = false;
  export let results = [];
  export let closeModal = () => {};

  console.log(results);
</script>

{#if showModal}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div class="modal-overlay" on:click={closeModal}></div>
  <div class="modal">
    <!-- svelte-ignore a11y-no-static-element-interactions -->

    <div class="modal-content">
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <span class="close" on:click={closeModal}>&times;</span>
      <table>
        <thead>
          <tr>
            <th> CITY </th>
            <th> WINS</th>
            <th> LOSSES </th>
          </tr>
        </thead>
        <tbody>
            <tr>
              <td>{results[2]}</td>
              <td>{results[3]}</td>
              <td>{results[4]}</td>
            </tr>
        </tbody>
      </table>
    </div>
  </div>
{/if}

<style>
  .modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: rgba(19, 19, 19, 0.901);
    padding: 20px;
    border: 1px solid #ff3e00;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
    z-index: 1000;
  }
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 999;
  }
</style>
