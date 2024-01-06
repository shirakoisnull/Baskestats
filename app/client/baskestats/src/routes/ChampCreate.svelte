<script>
  import { navigate } from "svelte-routing";

  let champ = {
    year: 0
  }

 async function handleSubmit() {
    // Logic for handling form submission (to be implemented)
    // Example: Send data to API, perform validation, etc.
 try {
      const response = await fetch('http://127.0.0.1:5004/championships', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          cYear: champ.year
        })
      });

      if (response.ok) {
        console.log('championship created successfully!');
        // Perform any necessary actions upon successful creation
      } else {
        console.error('Failed to create championship:', response.statusText);
      }
    } catch (error) {
      console.error('Error creating championship:', error);
    }
    navigate("/champ");
  }

  function handleCancel() {
    navigate("/champ");
  }

</script>

<h1>New Championship</h1>

<form on:submit|preventDefault={handleSubmit}>
  <label>
    Championship Year:
    <input type="number" min="1800" bind:value={champ.year} />
  </label>
  <button type="submit" class="submit-button">Submit</button>
  <button type="button" on:click={handleCancel}>Cancel</button>
</form>

<style>
  /* Style for vertical alignment and centering */
  form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 25vh;
    gap: 12px; /* Adjust vertical gap between form elements */
  }

  label {
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 300px; /* Adjust maximum width of form elements */
  }

  input,
  button {
    padding: 8px;
    margin-top: 6px;
    font-size: 1em;
    width: calc(
      100% - 16px
    ); /* Match the width of input/button to label width */
    /* Subtracting 16px (padding) from the width to account for padding */
  }

  button {
    margin-top: 5px; /* Adjust top margin of the buttons */
  }
 
</style>