var promiseAllSettled = function(functions) {
  return new Promise(resolve => {
    if(functions.length === 0) {
      resolve([]);
      return;
    }

    const res = new Array(functions.length).fill(null);
    let settledCounter = 0;

    const updateResultAndCheckResolve = (result, idx) => {
      res[idx] = result;
      settledCounter++;
      if(settledCounter === functions.length) resolve(res);
    };

    functions.forEach((func, idx) => {
      func().then(subRes => {
        updateResultAndCheckResolve({status: 'fulfilled', value: subRes}, idx);
      }, err => {
        updateResultAndCheckResolve({status: 'rejected', reason: err}, idx);
      });
    });
  });
};
