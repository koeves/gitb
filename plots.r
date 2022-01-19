## ORDER: DBG, RND, FFT
x = 1:3

# 32B cache line
hitrate_32 = c(28, 57, 15)
hitrate_64 = c(51, 87, 39)

reads_32 = c(40, 33031, 86298)
read_hit_32 = c(12, 19036, 13661)
read_miss_32 = c(28, 13995, 72637)

writes_32 = c(60, 32505, 43195)
write_hit_32 = c(16, 18631, 6700)
write_miss_32 = c(44, 13874, 36495)

read_hitmissrate_32 = c(read_hit_32[1]/read_miss_32[1], read_hit_32[2]/read_miss_32[2], read_hit_32[3]/read_miss_32[3])
write_hitmissrate_32 = c(write_hit_32[1]/write_miss_32[1], write_hit_32[2]/write_miss_32[2], write_hit_32[3]/write_miss_32[3])

# 64B cache line (32KiB cache size) -> 19 bit tags
reads_64 = c(40, 33031, 86298)
read_hit_64 = c(16, 28730, 33622)
read_miss_64 = c(24, 4301, 52676)

writes_64 = c(60, 32505, 43195)
write_hit_64 = c(35, 28235, 16412)
write_miss_64 = c(25, 4270, 26783)

read_hitmissrate_64 = c(read_hit_64[1]/read_miss_64[1], read_hit_64[2]/read_miss_64[2], read_hit_64[3]/read_miss_64[3])
write_hitmissrate_64 = c(write_hit_64[1]/write_miss_64[1], write_hit_64[2]/write_miss_64[2], write_hit_64[3]/write_miss_64[3])

# PLOTS (export: 4x4 in)
plot.default(
  x, hitrate_32,
  axes=F,
  pch=4,
  ylab="Hitrate [%]",
  xlab="Tracefile",
  main="Hitrates of tracefile executions",
  ylim=range(c(0, 100))
)
axis(side=1, at=x, labels=c("dbg", "rnd", "fft"))
axis(side=2, las=2, at=c(0, hitrate_32, hitrate_64, 100), labels=c(0, hitrate_32, hitrate_64, 100))
lines(x, hitrate_32, lty=2)
lines(x, hitrate_64,lty=3)
points(x, hitrate_64, pch=8)
legend("topright", 
       inset = 0.1,
       legend=c("32B", "64B"),
       lty=c(2,3), pch=c(4,8),  box.lwd = 0, bty="n", bg="transparent")
