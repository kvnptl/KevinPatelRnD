# Some useful things to note

1. How to run the bash script
```bash
sbatch name.sh
```

2. For `wr15` use `gpu4` instead of `gpu`

3. Check the current batch status (https://www.wr.inf.h-brs.de/wr/stat/batch.xhtml)

4. for datasets and large files, use the `/scratch/<username>` partition. Check your quota usage occasionally using `quota -s`

5. Use conda environments

5. when requesting jobs, don't forget to specify `--n-tasks-per-node` to be more than one if you need it (i.e. how many cores you want to use)

6. you cannot allocate GPU memory for your job, so you might have the case where you get allocated a GPU node already in use by someone, and your job dies because of insufficient GPU memory. In this case, increase (for example), the `--mem` (CPU memory) request to something like 64G. This will make sure you get an unused GPU node.

7. do not run any program which takes a lot of resources on wr0

8. For wr20-25, a special permission is required. the person to contact is Prof. Berrendorf (Rudolf.Berrendorf@h-brs.de)

9. For pre/post-processing, change the partition from `gpu` to `any`