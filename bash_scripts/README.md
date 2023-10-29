# Some useful things to note

1. How to run a bash script
```bash
sbatch name.sh
```

2. For `wr15` use `gpu4` instead of `gpu`

3. Check the current batch status (https://www.wr.inf.h-brs.de/wr/stat/batch.xhtml)

4. For datasets and large files, use the `/scratch/<username>` partition. Check your quota usage occasionally using `quota -s`

5. Use conda environments

6. When requesting jobs, don't forget to specify `--n-tasks-per-node` to be more than one if you need it (i.e. how many cores you want to use)

7. You cannot allocate GPU memory for your job, so you might have the case where you get allocated a GPU node already in use by someone, and your job dies because of insufficient GPU memory. In this case, increase (for example), the `--mem` (CPU memory) request to something like 64G. This will make sure you get an unused GPU node.

8. Do not run any program which takes a lot of resources on wr0

9. For wr20-25, a special permission is required. the person to contact is Prof. Berrendorf (Rudolf.Berrendorf@h-brs.de)

10. For pre/post-processing, change the partition from `gpu` to `any`

11. Information about job runs, `sacct -j 154672 -o jobid,submit,start,end,state`. Replace `154672` with your job ID. (Ref: [official documentation](https://wr0.wr.inf.h-brs.de/wr/usage.html#:~:text=fopen(all%2C%20%22w%22)%3B%0A%20%20%7D-,Information%20about%20Job%20Runs,-Sometimes%20it%20is))

12. Current job queue status, `squeue <jobid>`

13. To kill a job, `scancel <jobid>`

14. To check the current node, `echo `hostname``
