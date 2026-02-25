<template>
  <router-link :to="props.href" class="no-underline">
    <div class="desk-thumb w-full flex flex-col gap-2">
        <div class="aspect-w-1 aspect-h-1 bg-white rounded border-none">
            <div class="w-full h-full center">
                <span>icon</span>
            </div>
        </div>
        <div class="text-xs text-gray-900 text-center">{{ props.label }}</div>
    </div>
  </router-link>
</template>
<script setup lang="ts">

const props = withDefaults(
  defineProps<{
    label?: string,
    href?: string
  }>(),
  {
    label: "Department",
    href: "#"
  }
)

</script>