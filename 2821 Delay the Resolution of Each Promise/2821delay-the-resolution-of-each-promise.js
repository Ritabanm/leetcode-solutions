function delayAll(functions, ms) {
  const newFunctions = [];

  functions.forEach(el => {
    const newFuncWithPromise = () => {
      return new Promise((resolve, reject) => {
        // Introduce the delay
        setTimeout(() => {
          el()
            .then(res => {
              resolve(res);
            })
            .catch(err => {
              reject(err);
            });
        }, ms);
      });
    }

    // Add the new function with the delay to the results
    newFunctions.push(newFuncWithPromise);
  });

  return newFunctions;
};